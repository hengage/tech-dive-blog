from django import forms
from django.forms import widgets

from .models import Comment, Post, Comment
from .choices import CATEGORY_CHOICES


class CreatePostForm(forms.ModelForm):

    #field_order = ['body', 'title', 'description', 'author', 'category',]

    class Meta: 
        model = Post
        fields = ['title', 'description', 'category', 'body',]
    

        widgets ={
               'title': forms.TextInput(attrs={
                   'class':'form-control bigger-height'
                   }),

               'description': forms.TextInput(attrs={
                   'class':'form-control bigger-height'
                   }),

               'author': forms.TextInput(attrs={
                   'class':'form-control bigger-height',  'type':'hidden'
                   }),

               'category': forms.Select(choices=CATEGORY_CHOICES, attrs={
                   'class':'form-control bigger-height'
                   }),

               'body': forms.Textarea(attrs={
                   'class':'form-control', 'rows': 18
                   }),
        }


class EditPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'description', 'category', 'body',]

        widgets ={
               'title': forms.TextInput(attrs={
                   'class':'form-control bigger-height'
                   }),

               'description': forms.TextInput(attrs={
                   'class':'form-control bigger-height'
                   }),

               'category': forms.Select(choices=CATEGORY_CHOICES, attrs={
                   'class':'form-control bigger-height'
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
            'comment_body': forms.Textarea(attrs={
                'class': 'add-comment-box',
                # 'rows': 43,
                # 'cols':59
            })
        }

        