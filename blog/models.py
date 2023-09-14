from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from cloudinary.models import CloudinaryField
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse


STATUS = ((0, "Draft"), (1, "Published"))
User = get_user_model()


class Category(models.Model):
    """
    Model for category
    """

    title = models.CharField(max_length=20)
    category_image = CloudinaryField('image', default='placeholder')
    slug = models.SlugField(max_length=100, unique=True, default="", null=True)
    excerpt = models.TextField(blank=True)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.title


class Post(models.Model):
    """
    Model for the main blog post
    """

    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True, null=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts"
    )
    categories = models.ManyToManyField(Category, blank=True)
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    excerpt = models.TextField(blank=True)
    featured_image = CloudinaryField("image", default="placeholder")
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(
        User, related_name="blogpost_likes", blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    comment_count = models.IntegerField(default=0)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.title + " | " + str(self.author)

    def number_of_likes(self):
        return self.likes.count()
        


class Comment(models.Model):
    """
    Model for post comments
    """
    post = models.ForeignKey(Post, on_delete=models.CASCADE,
                             related_name="comments")
    name = models.CharField(max_length=100)
    email = models.EmailField()
    approved = models.BooleanField(default=False)
    body = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Comment {self.body} by {self.name}"
    
    def get_absolute_url(self):
        return reverse('post_detail', args=[self.post.slug])


STATUS = ((0, "Draft"), (1, "Published"))
User = get_user_model()


class UserProfile(models.Model):
    """
    Model for user profile

    """

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    user = models.OneToOneField(User, on_delete=models.CASCADE,
                                related_name='profile')
    presentation = models.TextField(max_length=500)
    image = CloudinaryField('image', default='default_image')

    def __str__(self):
        return f'{self.user.username} Profile'


class Author(models.Model):
    """
    Model for author
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    author_picture = CloudinaryField('image', default='placeholder')

    def __str__(self):
        return self.user.username
