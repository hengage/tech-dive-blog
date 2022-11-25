from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from django.template.defaultfilters import slugify
import random
from django.core.exceptions import ValidationError

from .managers import CustomUserManager


def validate_field_has_no_whitesapce(value):
    """
    Check if model fields have whitespaces"""
    if value.find(' ') != -1:

    # t = value.split()
    # if len(t) > 1:
        raise ValidationError(
            _("This field cannot contain spaces")
        )


class CustomUser(AbstractBaseUser, PermissionsMixin):
    username = None
    email = models.EmailField(_("email address"), unique=True)
    first_name = models.CharField(max_length=150, validators=[ validate_field_has_no_whitesapce ])
    last_name = models.CharField(max_length=150,  validators=[ validate_field_has_no_whitesapce ])
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

    def save(self, *args, **kwargs): 
        random_string = ''.join(str(random.randint(0, 9)) for _ in range(5))
        slug = f'{self.first_name}{self.last_name}{random_string}'
        if not self.slug:
            self.slug = slugify(slug)
        return super().save(*args, **kwargs)