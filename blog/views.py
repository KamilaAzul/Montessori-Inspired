from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic, View
from django.views.generic import CreateView, UpdateView, DeleteView
from django.http import HttpResponseRedirect
from .models import Post, UserProfile, Comment, Category
from django.utils.text import slugify
from django.contrib import messages
from django.db.models import Q
from django.views.generic import UpdateView
from .forms import PostForm,  ProfileUpdateForm, UserUpdateForm, CommentForm
from .forms import UpdatePostForm
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required


class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by("-created_on")
    template_name = "index.html"
    paginate_by = 6


class PostDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by("-created_on")
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": False,
                "liked": liked,
                "comment_form": CommentForm()
            },
        )

    def post(self, request, slug, *args, **kwargs):

        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by("-created_on")
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
        else:
            comment_form = CommentForm()

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": True,
                "comment_form": comment_form,
                "liked": liked
            },
        )


class AllBlogPost(generic.ListView):
    """
    Render the blog page
    """
    model = Post
    queryset = Post.objects.filter(status=1).order_by("-created_on")
    template_name = "blog.html"
    paginate_by = 9


class PostLike(View):

    def post(self, request, slug, *args, **kwargs):
        post = get_object_or_404(Post, slug=slug)
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        return HttpResponseRedirect(reverse('post_detail', args=[slug]))


def about(request):
    """
    Render the about page
    """
    return render(request, "about.html")


def categories(request):
    """
    Renders the categories page
    """
    return render(request, 'categories.html')


def categories_view(request, categ):
    """
    Renders the posts filtered by categories
    """
    categories_posts = Post.objects.filter(
        categories__title__contains=categ, status=1)

    return render(
        request,
        "categories_post.html",
        {"categ": categ.title(), 'categories_posts': categories_posts},
    )


class AddCategoriesView(CreateView):
    model = Category
    template_name = "categories_post.html"
    fields = ('title',)


def search(request):
    """
    search results
    """
    queryset = request.GET.get('q')
    post = Post.objects.filter(Q(title__icontains=queryset) |
                               Q(content__icontains=queryset))
    if not post:
        messages.warning(request,
                         f'Your search for "{queryset}" returned no resuts')
    context = {
        "posts": post,
        'queryset': queryset
    }

    return render(request, 'search.html', context)


class DeletePost(generic.DeleteView):
    """
    Class to allow to delete a post
    """
    model = Post
    template_name = "delete_post.html"
    success_message = "Post was deleted successfully."

    def delete(self, request, *args, **kwargs):
        messages.warning(self.request, self.success_message)
        return super(DeletePost, self).delete(request, *args, **kwargs)

    def get_success_url(self):
        """
        Set the reverse url for the successful delete
        of the post to the database
        """
        return reverse("user-posts")


@login_required()
def update_post(request, slug):
    """
    Users can update their blog post that they have created
    """
    post = get_object_or_404(Post, slug=slug)
    if request.user.id == post.author.id:
        if request.method == "POST":
            form = UpdatePostForm(request.POST, request.FILES, instance=post)
            if form.is_valid():
                post = form.save(commit=False)
                post.author = request.user
                post.slug = slugify(post.title)
                post.status = 1
                form.save()
                messages.success(
                    request, "Your post was updated successfully!")
                return redirect(reverse("user-posts"))
            else:
                messages.error(request, "Failed to update the post.")
        else:
            form = UpdatePostForm(instance=post)
    else:
        messages.error(request, "Sorry, This is not your post.")

    template = ("update_post.html",)
    context = {"form": form, "post": post}
    return render(request, template, context)


@login_required
def create_post(request):
    context = {}
    form = PostForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            print("\n\n form is valid")
            new_post = form.save(commit=False)
            new_post.author = request.user
            new_post.save()

            return redirect('blog')

    context.update({
        'form': form,
        'title': 'Create New Post'
    })
    return render(request, 'new_post.html', context)


class UserPost(LoginRequiredMixin, generic.ListView):
    """
    Shows all posts of a logged-in user in one page
    """
    model = Post
    author = Post.author
    template_name = "user_posts.html"

    def get_queryset(self, *args, **kwargs):
        return Post.objects.filter(
            author=self.request.user, status=1).order_by(
            "-created_on"
        )


class EditComment(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    """
    Edit comment
    """
    model = Comment
    template_name = 'edit_comment.html'
    form_class = CommentForm
    success_message = 'The comment was successfully updated'

    def get_success_url(self):
        """
        Set the reverse url for the successful edit of comment
        of the post to the database
        """
        return reverse("user-posts")


@login_required
def delete_comment(request, comment_id):
    """
    Delete comment
    """
    comment = get_object_or_404(Comment, id=comment_id)
    comment.delete()
    messages.success(request, 'The comment was deleted successfully')
    return HttpResponseRedirect(reverse(
        'post_detail', args=[comment.post.slug]))
