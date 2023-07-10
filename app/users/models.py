from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager
from .managers import CustomUserManager

# Create your models here.
# class AuthorBlog(AbstractBaseUser, PermissionsMixin):
class AuthorBlog(models.Model):
    name = models.CharField(max_length=50,unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=50)
    is_staff = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)

    # objects = CustomUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []