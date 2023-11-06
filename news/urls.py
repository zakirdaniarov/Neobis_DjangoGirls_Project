from django.urls import path
from .views import postView, addPost, editPost

urlpatterns = [
    path('', postView),
    path('create_post/', addPost),
    path('edit_post/<int:i>/', editPost),
]
