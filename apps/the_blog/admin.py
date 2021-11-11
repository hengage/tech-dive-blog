from django.contrib import admin
from .models import Post, PostCategory, Comment

from markdownx.admin import MarkdownxModelAdmin

class CommentInline(admin.StackedInline):
    model = Comment
    extra= 0

class PostAdmin(admin.ModelAdmin):
    inlines = [
        CommentInline
    ]
admin.site.register(Post, PostAdmin) 
# admin.site.register(Post, MarkdownxModelAdmin)  
admin.site.register(PostCategory)
admin.site.register(Comment,MarkdownxModelAdmin)
