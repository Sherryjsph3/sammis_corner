from functools import total_ordering
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Post


# Create your views here.


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')

def jewelry(request):
    return render(request, 'jewelry.html')

def beauty(request):
    return render(request, 'beauty.html')


#Class base views
class PostIndex(ListView):
    model = Post
    template_name = 'index.html'
    context_object_name = 'posts'

class PostDetail(DetailView):
    model = Post
    template_name = 'detail.html'
    context_object_name = 'post'    

class PostCreate(CreateView):
    model = Post
    fields = ['title', 'image_one', 'image_two', 'blurb', 'status']
    template_name = 'new.html'
    success_url = '/posts/'

class PostDelete(DeleteView):
    model = Post
    template_name = 'confirm_delete.html'
    success_url = '/posts/'

class PostUpdate(UpdateView):
    model = Post
    fields = ['title', 'image_one', 'image_two', 'blurb', 'status']
    template_name = 'new.html'
    success_url = '/posts/'