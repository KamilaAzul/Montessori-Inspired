from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.views.generic import CreateView, UpdateView, DeleteView
from django.http import HttpResponseRedirect
from .models import Post
from .forms import CommentForm
from django.db.models import Q
from django.views.generic import UpdateView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin


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
    return render(request, 'categories_posts.html', {
        'categ': categ.title(), 'categories_posts': categories_posts})


def categories_list(request):
    """Return a list of destinations for the dropdown in the navbar"""

    categories = Category.objects.all()
    context = {
        'categories': categories
    }
    return context


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
        "posts": post
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
        return reverse("user-post-list")
