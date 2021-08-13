
from django.contrib.auth import forms
from django.http import HttpResponseRedirect, request
from django.shortcuts import redirect, render, get_object_or_404
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse
from.forms import CommentForm, PostForm, UpdateForm, PhotoForm
from .models import Comment, Post, Photo

import boto3
import uuid

S3_BASE_URL= 'https://s3-us-east-2.amazonaws.com/'
BUCKET= 'sammis-corner-new'


# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def jewelry(request):
    return render(request, 'jewelry.html')

def beauty(request):
    return render(request, 'beauty.html')

def register(request):
    errors = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
        else:
            errors = form.errors

    form = UserCreationForm
    return render(request, 'registration/register.html', {
        'form': form,
        'errors': errors
        }) 

def search_posts(request):
    if request.method == 'POST':
        searched = request.POST[ 'searched']
        posts = Post.objects.filter(blurb__contains=searched)
        return render(request, 
        'search_posts.html', 
        {'searched': searched,
        'posts': posts})
    else:
        return render(request, 
        'search_posts.html', {})

def LikeView(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    post.likes.add(request.user)
    return HttpResponseRedirect(reverse('post-detail', args=[str(pk)]))


def add_photo(request, post_id):
    photo_file = request.FILES.get('photo-file', None)
    if photo_file:
        s3 = boto3.client('s3')
        key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
        try:
            s3.upload_fileobj(photo_file, BUCKET, key)
            url = f"{S3_BASE_URL}{BUCKET}/{key}"
            photo = Photo(url=url, post_id=post_id)
            photo.save()
        except Exception as error:
            print('An error occurred uploading file to S3')
            print(error)
    return redirect('post-detail', post_id=post_id)

#Class base views
class PostIndex(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'index.html'
    context_object_name = 'posts'

    # def get_queryset(self):
    #     return Post.objects.filter(user=self.request.user)

    
class PostDetail(LoginRequiredMixin, DetailView):
    model = Post
    template_name = 'detail.html'
    context_object_name = 'post' 

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        stuff = get_object_or_404(Post, id=self.kwargs['pk'])
        total_likes = stuff.total_likes()
        context["total_likes"] = total_likes
        return context   

class PostCreate(LoginRequiredMixin, CreateView):
    model = Post
    # fields = ['title', 'image_one', 'image_two', 'blurb', 'status']
    form_class = PostForm
    second_form_class = PhotoForm
    template_name = 'new.html'
    success_url = '/posts/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class AddCommentView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'add_comment.html'
    success_url = '/posts/'

    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)

class PostDelete(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = 'confirm_delete.html'
    success_url = '/posts/'

class PostUpdate(LoginRequiredMixin, UpdateView):
    model = Post
    # fields = ['title', 'image_one', 'image_two', 'blurb', 'status']
    form_class = UpdateForm
    template_name = 'edit.html'
    success_url = '/posts/'