# Testing

Back to the [README](README.md)

# Table of Contents
- [User Story Testing](#user-story-testing)
- [Validator Testing](#validator-testing)
  * [HTML](#html)
    + [Fixed Errors](#fixed-errors)
    + [Unfixed Errors](#unfixed-errors)
  * [CSS](#css)
  * [Javascript](#javascript)
  * [Python](#python)
  * [Lighthouse](#lighthouse)
- [Browser Testing](#browser-testing)
- [Device Testing](#device-testing)
- [Manual Testing](#manual-testing)
  * [Site Navigation](#site-navigation)
  * [Home Page](#home-page)
  * [Browse Recipes Page](#browse-recipes-page)
  * [Recipe Detail Page](#recipe-detail-page)
  * [Add Recipe Page](#add-recipe-page)
  * [Update Recipe Page](#update-recipe-page)
  * [Confirm Delete Recipe Page](#confirm-delete-recipe-page)
  * [My Recipes Page](#my-recipes-page)
  * [My Bookmarks Page](#my-bookmarks-page)
  * [My Meal Plan Page](#my-meal-plan-page)
  * [Django All Auth Pages](#django-all-auth-pages)
- [Bugs](#bugs)
  * [Fixed Bugs](#fixed-bugs)
    + [Overwrite Meal Plan Items](#overwrite-meal-plan-items)
    + [Required fields using Summernote extension submit with just whitespace entered](#required-fields-using-summernote-extension-submit-with-just-whitespace-entered)
    + [No Reverse Match Error](#no-reverse-match-error)
    + [Cloudinary Images not Displaying](#cloudinary-images-not-displaying)
    + [Footer not staying at bottom of screen](#footer-not-staying-at-bottom-of-screen)
  * [Unfixed bugs:](#unfixed-bugs-)

<small><i><a href='http://ecotrust-canada.github.io/markdown-toc/'>Table of contents generated with markdown-toc</a></i></small>

## User Story Testing


## Validator Testing

### HTML

All HTML pages were run through the [W3C HTML Validator](https://validator.w3.org/). See results in below table.

| Page                 | Logged Out | Logged In |
|----------------------|------------|-----------|
| base.html            | No errors  | No errors |
| index.html           | No errors  | No errors |
| about.html           | No errors  | No errors |
| blog.html            | N/A        | No errors |
| new_post.html        | N/A        | No errors |
| post_detail.html     | N/A        | No errors |
| search.html          | N/A        | No errors |
| user_profile.html    | N/A        | No errors |
| user_posts.html      | N/A        | No errors |
| edit_comment.html    | N/A        | No errors |
| update_post.html     | N/A        | Note 1    |
| delete_post.html     | N/A        | Note 1    |
| delete_comment.html  | N/A        | Note 1    |
| login.html           | No errors  | N/A       |
| logout.html          | N/A        | No errors |
| signup.html          | No errors  | N/A       |


class EditPost(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    """
    Edit Post
    """
    model = Post
    form_class = PostForm
    template_name = 'update_post.html'
    success_message = 'The post was successfully updated'

    def get_success_url(self):
        """
        Set the reverse url for the successful delete
        of the post to the database
        """
        return reverse("user-posts")

@login_required()
def update_post(request, slug):
    """
    Update the blog post 
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
                return HttpResponseRedirect(reverse(
                    'post_detail'))
            else:
                messages.error(request, "Failed to update the post.")
        else:
            form = UpdatePostForm(instance=post)
    else:
        messages.error(request, "Sorry, This is not your post.")

    template = ("update_post.html",)
    context = {"form": form, "post": post}
    return HttpResponseRedirect(reverse('post_detail', args=[slug]))
