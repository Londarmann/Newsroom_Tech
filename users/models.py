from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager
from tinymce.models import HTMLField


class User(AbstractUser, PermissionsMixin):
    email = models.EmailField(_("email address"), unique=True)
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    image = models.FileField(null=True, upload_to='media/')
    is_author = models.BooleanField(null=False, default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    description = HTMLField(blank=True, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email



