from django import forms
from django.forms import widgets

from .models import Comment, Post, Comment


class CreatePostForm(forms.ModelForm):

    #field_order = ['body', 'title', 'description', 'author', 'category',]
    class Meta: 
        model = Post
        fields = ['title', 'description', 'body',]
    
        widgets ={
               'title': forms.TextInput(attrs={
                   'class':'form-control'
                   }),

               'description': forms.TextInput(attrs={
                   'class':'form-control'
                   }),

               'author': forms.TextInput(attrs={
                   'class':'form-control',  'type':'hidden'
                   }),

               'body': forms.Textarea(attrs={
                   'class':'form-control', 'rows': 18
                   }),
        }

class EditPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'description', 'body',]

        widgets ={
               'title': forms.TextInput(attrs={
                   'class':'form-control'
                   }),

               'description': forms.TextInput(attrs={
                   'class':'form-control'
                   }),

               'body': forms.Textarea(attrs={
                   'class':'form-control', 'rows': 18
                   }),
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment_body',]

        widgets = {
            'comment_body': forms.Textarea(attrs={})
            }

        