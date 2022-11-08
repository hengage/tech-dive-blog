from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.conf import settings
from django.template.defaultfilters import slugify
from django.db.models.signals import pre_save

from markdownx.models import MarkdownxField
from markdownx.utils import markdownify

from .managers import PostManager
from simple_blog.utils import unique_slug_generator
class Category(models.Model):
    category_name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=70, null=True, blank=True, editable=False)

    def __str__(self):
        return f"{self.category_name}"
    class Meta: 
        verbose_name = 'category'
        verbose_name_plural = 'categories'


def pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

pre_save.connect(pre_save_receiver, sender=Category)

class Post(models.Model):
    title = models.CharField(max_length=255, unique=True)
    description = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255, unique=True)
    category = models.ForeignKey(
        Category, 
        on_delete=models.PROTECT,
        related_name='category',
        default=1
    )
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE,
        related_name='author',
        default=''
    )
    body = MarkdownxField()
    likes = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name='blog_posts',
        blank=True
        )
    objects = PostManager()

    class Meta:
        ordering = ['-date_created']


    def formatted_markdown(self):
        return markdownify(self.body)

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
    comment_body = MarkdownxField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def formatted_markdown(self):
        return markdownify(self.comment_body)

    def __str__(self):
        return f"{self.comment_body}| {self.post}"

    def get_absolute_url(self):
        return reverse('article_detail', kwargs={'pk':self.pk})
