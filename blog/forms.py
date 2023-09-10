from .models import UserProfile
from django.contrib.auth.models import User
from django.forms import ModelForm
from django import forms
from .models import Comment, Post, UserProfile, Category

# categ = [('home ideas', 'home ideas'), ('books', 'books'), ('nature', 'nature'),
# ('toys', 'toys'), ('art', 'art'), ('music', 'music'), ('activities', 'activities'), ('parenting tips', 'parenting tips')]

categ = Category.objects.all().values_list("title", "title")

categ_list=[]

for item in categ:
    categ_list.append(item)

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
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "author": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "type": "hidden"
                }
            ),
            "categories": forms.Select(choices=categ_list, attrs={"class": "form-control"}),

        }


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
