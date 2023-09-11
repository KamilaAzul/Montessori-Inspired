from .models import UserProfile
from django.contrib.auth.models import User
from django.forms import ModelForm
from django import forms
from .models import Comment, Post, UserProfile, Category


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


class CommentForm(forms.ModelForm):
    """
    Form for post comments
    """
    class Meta:
        model = Comment
        fields = ('body', )


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
            "featured_image",
        )


class UserUpdateForm(forms.ModelForm):
    """
    Form for profile name update
    """
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    """
    Form for profile image update
    """
    class Meta:
        model = UserProfile
        fields = ['image']
