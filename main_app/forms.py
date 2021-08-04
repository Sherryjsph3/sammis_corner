from django import forms
from django.forms import widgets
from .models import Comment, Post

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
        fields = ('title', 'image_one', 'image_two', 'blurb', )

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-post-two'}),
            'image_one': forms. ClearableFileInput(attrs={'class': 'form-post'}),
            'image_two': forms. ClearableFileInput(attrs={'class': 'form-post'}),
            'blurb': forms.Textarea(attrs={'class': 'form-control-two'}),

        } 
               