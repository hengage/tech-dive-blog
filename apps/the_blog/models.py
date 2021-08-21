from django.db import models
#from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.db.models.deletion import CASCADE
from django.db.models.fields import TextField
from django.urls import reverse
from django.conf import settings
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
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, default='')
    category = models.CharField(max_length=50, default='No category')
    body = TextField()
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
        return reverse('article_detail', kwargs={'pk':self.pk}) # args=[str(self.id)]


class Comment(models.Model):
    post = models.ForeignKey(Post,
     on_delete=models.CASCADE,
    related_name='comments'
    )
    commentator = models.ForeignKey(get_user_model(),
        on_delete=models.CASCADE
    )
    comment_body = models.TextField(max_length=1000)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.comment_body}| {self.post}"

    def get_absolute_url(self):
        return reverse('article_detail', kwargs={'pk':self.pk})
