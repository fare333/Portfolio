from django.urls import path

from . import views

urlpatterns = [
    path('', views.home,name="home"),
    path("posts/",views.posts,name="posts"),
    path("post/<str:slug>/",views.post,name="post"),
    path("profile/",views.profile,name="profile"),
    path("post-form/",views.createPost,name="post_form"),
    path("post-update/<str:slug>/",views.updatePost,name="post_update"),
    path("post-delete/<str:slug>/",views.deletePost,name="post_delete"),
    path("send_email/",views.send_email,name="send_email")
]