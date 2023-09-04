from .models import Comment
from django import forms
from .models import Post
from django.forms import ModelForm
from django.contrib.auth.models import User
from django import forms


class CommentForm(forms.ModelForm):
    """
    Form for post comments
    """
    class Meta:
        model = Comment
        fields = ('body', )


class PostForm(forms.ModelForm):
    """
    Form to add a blog post
    """
    class Meta:
        model = Post
        fields = (
            "title",
            "categories",
            "content",
             "featured_image",
        )
        


class UpdatePostForm(forms.ModelForm):
    """
    Form to edit a blog post
    """

    class Meta:
        model = Post
        fields = (
            "title",
            "categories",
            "content",
        )
