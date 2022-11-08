from django.contrib import admin
from .models import Post,  Comment, Category

from markdownx.admin import MarkdownxModelAdmin

class CommentInline(admin.StackedInline):
    model = Comment
    extra= 0

class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'date_created']
    inlines = [ CommentInline ]

class PostInline(admin.StackedInline):
    model = Post
    extra = 0

class CategoryAdmin(admin.ModelAdmin):
    model = Category
    list_display = ['category_name', 'id', 'slug']
    inlines = [  PostInline ]

admin.site.register(Post, PostAdmin) 
admin.site.register(Category, CategoryAdmin)
# admin.site.register(Post, MarkdownxModelAdmin)  
admin.site.register(Comment,MarkdownxModelAdmin)
