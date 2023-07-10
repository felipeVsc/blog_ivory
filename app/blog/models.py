from django.db import models
from datetime import date
from ..users.models import AuthorBlog
from django.contrib.auth.models import User
# Create your models here.

class Blog(models.Model):
    author = models.ForeignKey(User,on_delete=models.CASCADE,unique=True)
    name = models.CharField(max_length=50)
    active = models.BooleanField(default=True)
    description = models.CharField(max_length=500)
    created_at = models.DateField(default=date.today)

