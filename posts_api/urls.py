from django.urls import path
from . import views

urlpatterns = [
    #path('', views.routes),
    path('posts', views.posts_api),
    path('posts/<str:post_id>/', views.post_api),
    path('create', views.create_post),
    path('posts/<str:post_id>/edit', views.edit_post),
    path('posts/<str:post_id>/delete', views.delete_post),
]
