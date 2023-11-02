from django.shortcuts import render
from django.views import generic
from .forms import PostForms
from .models import PostsModel
from django.http import HttpResponseRedirect

# Create your views here.

def postView(request):
    form = PostsModel.objects.filter().order_by('-id')
    return render(request, 'index.html', {'all_items': form})

def addPost(request):
    obj = PostsModel()
    if request.method == "POST":
        form = PostForms(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = PostForms(instance=obj)

    return render(request, 'create_post.html', {'form': form})

def editPost(request, i):
    obj = PostsModel.objects.get(id=i)
    if request.method == "POST":
        form = PostForms(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = PostForms(instance=obj)

    return render(request, 'edit_post.html', {'form': form})

def deletePost(request, i):
    obj = PostsModel.objects.get(id=i)
    obj.delete()
    return HttpResponseRedirect('/')






