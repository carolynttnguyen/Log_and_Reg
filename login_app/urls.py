from django.urls import path, include
from . import views

urlpatterns=[
    path('', views.index),
    path('create_user', views.register),
    path('login', views.login),
    path('wall', views.view_wall),
    path('post-message', views.post_message),
    path('post-comment/<int:id>', views.post_comment),
    path('success', views.success),
    path('logout', views.logout),
]