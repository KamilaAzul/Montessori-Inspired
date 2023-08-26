from . import views
from django.urls import path

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
    path("about", views.about, name="about"),
    path('categories', views.categories, name="categories"),
    path('categories_posts<str:categ>', views.categories_view,
         name="categories_posts"),
    path("blog", views.AllBlogPost.as_view(), name="blog"),
    path('search/', views.search, name="search"),
]
