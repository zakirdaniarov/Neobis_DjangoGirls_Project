from .models import PostsModel
from django import forms

class PostForms(forms.ModelForm):
    class Meta:
        model = PostsModel
        fields = '__all__'
