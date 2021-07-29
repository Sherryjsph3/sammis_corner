from django.shortcuts import render
from django.views.generic import ListView
from .models import Post


# Create your views here.


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html') 


#Index Page as a Class based view
class PostIndex(ListView):
    model = Post
    template_name = 'index.html'
    context_object_name = 'posts'