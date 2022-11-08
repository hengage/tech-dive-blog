from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from django.db.models.signals import pre_save

from .managers import CustomUserManager
from simple_blog.utils import unique_slug_generator
class CustomUser(AbstractBaseUser, PermissionsMixin):
    username = None
    email = models.EmailField(_("email address"), unique=True)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    slug = models.SlugField(max_length=70, null=True, blank=True, editable=False)
    date_joined = models.DateTimeField(default=timezone.now)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    objects = CustomUserManager()

    USERNAME_FIELD = "email"

    REQUIRED_FIELDS = ["first_name", "last_name"]

    class Meta:
        ordering = ("email",)
        verbose_name = "user"
        verbose_name_plural = "users"

    def __str__(self):
        return f"{self.first_name.title()} {self.last_name.title()} - {self.email}"



def pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

pre_save.connect(pre_save_receiver, sender=CustomUser)