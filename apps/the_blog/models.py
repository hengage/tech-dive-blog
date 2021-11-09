from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.conf import settings
from django.template.defaultfilters import slugify
#from .choices import CATEGORY_CHOICES

class PostCategory(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
            return f"{self.name}"

    def get_absolute_url(self):
        return reverse('home')
    class Meta:
        verbose_name = ("Posts' Category")
        verbose_name_plural = ("Posts' Categories")


class Post(models.Model):
    title = models.CharField(max_length=255, unique=True)
    title_tag = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255, unique=True)
    category = models.ForeignKey(PostCategory, 
        on_delete=models.PROTECT,
        related_name='category',
        default='django'
    )
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE,
        related_name='author',
        default=''
    )
    body = models.TextField()
    likes = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name='blog_posts',
        blank=True
        )

    class Meta:
        ordering = ['-date_created']

    def __str__(self):
            return f"{self.title} | {str(self.author).title()}"


    def get_absolute_url(self):
        return reverse('article_detail', kwargs={'slug':self.slug}) # args=[str(self.slug)]

    def save(self, *args, **kwargs): 
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)


class Comment(models.Model):
    post = models.ForeignKey(Post,
     on_delete=models.CASCADE,
    related_name='comments'
    )
    commentator = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    comment_body = models.TextField(max_length=1000)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.comment_body}| {self.post}"

    def get_absolute_url(self):
        return reverse('article_detail', kwargs={'pk':self.pk})
