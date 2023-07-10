from django.db import models
from datetime import date
from ..blog.models import Blog
# Create your models here.
class Post(models.Model):
    blog = models.ForeignKey(Blog,on_delete=models.CASCADE)
    title = models.CharField(max_length=200,null=False)
    text = models.TextField()
    description = models.CharField(max_length=500)
    likes = models.IntegerField(default=0)
    published = models.BooleanField(default=False)
    created_at = models.DateField(default=date.today)
    deleted_at = models.DateField(null=True) # ver se tem forma melhor de fazer ambos (created)

class Reply(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE) # change this relation
    name = models.CharField(max_length=50)
    text = models.TextField()
    likes = models.IntegerField(default=0)
    created_at = models.DateField(default=date.today)


