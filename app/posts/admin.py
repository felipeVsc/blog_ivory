from django.contrib import admin
from .models import Post
from ..blog.models import Blog
from django import forms

# Register your models here.
@admin.action(description='Publish Post')
def publish_posts(modeladmin, request, queryset):
    queryset.update(published=True)


@admin.action(description='Archive Post')
def archive_posts(modeladmin, request, queryset):
    queryset.update(published=False)

class PostForm(forms.ModelForm):
    def __init__(self,*args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        self.fields['blog'].queryset = Blog.objects.filter(author=self.user)

class PostAdmin(admin.ModelAdmin):
    actions = [
        publish_posts,
        archive_posts
    ]

    list_display = [
        "published",
        "title",
        "created_at"
    ]
    exclude = ['created_at',"likes","deleted_at"]

    def get_queryset(self, request):
        if request.user.is_authenticated:
            return super().get_queryset(request).filter(blog__author=request.user)

        return super().get_queryset(request).none()

admin.site.register(Post,PostAdmin)