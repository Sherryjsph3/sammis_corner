from django import forms
from django.forms import widgets
from .models import Comment, Post, Photo

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields =('name', 'body')

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control-two'})
        }

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'blurb', )

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-post-two'}),
            'blurb': forms.Textarea(attrs={'class': 'form-control-two'}),

        } 

class UpdateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'blurb', )

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-update-two'}),
            'blurb': forms.Textarea(attrs={'class': 'form-update-three'}),

        } 

class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ['url']

        widgets = {
            'url': forms.TextInput(attrs={'class': 'form-upload'})
        }
            
              