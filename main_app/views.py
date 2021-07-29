
from django.shortcuts import redirect, render
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
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


#Class base views
class PostIndex(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'index.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return Post.objects.filter(user=self.request.user)

class PostDetail(LoginRequiredMixin, DetailView):
    model = Post
    template_name = 'detail.html'
    context_object_name = 'post'    

class PostCreate(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'image_one', 'image_two', 'blurb', 'status']
    template_name = 'new.html'
    success_url = '/posts/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class PostDelete(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = 'confirm_delete.html'
    success_url = '/posts/'

class PostUpdate(LoginRequiredMixin, UpdateView):
    model = Post
    fields = ['title', 'image_one', 'image_two', 'blurb', 'status']
    template_name = 'new.html'
    success_url = '/posts/'