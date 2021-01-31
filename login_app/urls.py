from django.urls import path, include
from . import views

urlpatterns=[
    path('', views.index),
    path('create_user', views.register),
    path('login', views.login),
    path('success', views.success),
    path('logout', views.logout),
]