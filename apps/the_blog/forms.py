from django import forms
from django.forms import widgets

from .models import Comment, Post, PostCategory, Comment
from .choices import CATEGORY_CHOICES


class PostForm(forms.ModelForm):
    """
        A form class to create posts
        
    """
    #field_order = ['body', 'title', 'title_tag', 'author', 'category',]

    class Meta: 
        model = Post
        fields = ['title', 'title_tag', 'category', 'body',]
    

        widgets ={
               'title': forms.TextInput(attrs={
                   'class':'form-control bigger-height', 'placeholder':'title'
                   }),
               'title_tag': forms.TextInput(attrs={
                   'class':'form-control bigger-height'
                   }),
               'author': forms.TextInput(attrs={'class':'form-control bigger-height',  'type':'hidden'}),
               'category': forms.Select(choices=CATEGORY_CHOICES, attrs={'class':'form-control bigger-height'}),
               'body': forms.Textarea(attrs={'class':'form-control', 'rows': 18}),
        }


class UpdateForm(forms.ModelForm):
    """
        A form class to update posts
    """
    class Meta:
        model = Post
        fields = ['title', 'title_tag', 'category', 'body',]

        widgets ={
               'title': forms.TextInput(attrs={
                   'class':'form-control bigger-height'
                   }),
               'title_tag': forms.TextInput(attrs={
                   'class':'form-control bigger-height'
                   }),
               'category': forms.Select(choices=CATEGORY_CHOICES, attrs={
                   'class':'form-control bigger-height'
                   }),
               'body': forms.Textarea(attrs={
                   'class':'form-control', 'rows': 18
                   }),
        }

        
#class UpdateForm(PostForm):
 #   fields = ['title', 'title_tag', 'category',]
 
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

        