from . import views
from django.urls import path

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
    path("about", views.about, name="about"),
    path('categories', views.categories, name="categories"),
    path('categories_posts<str:categ>', views.categories_view,
         name="categories_posts"),
    path("blog", views.AllBlogPost.as_view(), name="blog"),
    path('search/', views.search, name="search"),
    path('new_post/', views.create_post, name='new_post'),
    path("update_post/<slug:slug>/", views.update_post, name="update-post"),
    path(
        "delete_post/<slug:slug>/",
        views.DeletePost.as_view(),
        name="delete-post",
    ),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
]
