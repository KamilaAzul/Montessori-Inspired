from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
    path('user_profile', views.UserProfile.as_view(), name='user-profile'),
    path('edit_comment/<int:pk>', views.EditComment.as_view(),
         name='edit_comment'),
    path('delete_comment/<int:comment_id>', views.delete_comment,
         name='delete_comment'),
    path("about", views.about, name="about"),
    path('categories', views.categories_view, name="categories"),
    path('categories_posts<str:categ>', views.AddCategoriesView.as_view(),
         name="categories_posts"),
    path('blog', views.AllBlogPost.as_view(), name='blog'),
    path('search/', views.search, name="search"),
    path('new_post/', views.create_post, name='new_post'),
    path(
        "user_posts/", views.UserPost.as_view(), name="user-posts"
    ),
    path("update_post/<slug:slug>/", views.update_post, name="update-post"),
    path(
        "delete_post/<slug:slug>/",
        views.DeletePost.as_view(),
        name="delete-post",
    ),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
