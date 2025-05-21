from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.display_blogposts, name='display_blogposts'),
    path('create/', views.create_blogpost, name='create_blogpost'),
]