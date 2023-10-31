from django.db import models

class PostsModel(models.Model):
    title = models.CharField(max_length=500, verbose_name='Please enter the post title')
    content = models.TextField(verbose_name='Please enter the post text')
    createdDate = models.DateField()
# Create your models here.
