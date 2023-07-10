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
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if user:
            print("HER E WIHT")
            self.fields['blog'].queryset = Blog.objects.filter(author=user)


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

    form = PostForm
    def get_form(self, request, obj=None, **kwargs):
        if request.user.is_superuser:
            kwargs["form"] = PostForm
        return super().get_form(request, obj, **kwargs)

    def get_queryset(self, request):
        # Verifica se o usuário está autenticado
        if request.user.is_authenticated:
            # Filtra os objetos pela foreign key "blog" pertencente ao usuário
            print("here ne")
            return super().get_queryset(request).filter(blog__author=request.user)

        # Retorna uma queryset vazia se o usuário não estiver autenticado
        return super().get_queryset(request).none()

admin.site.register(Post,PostAdmin)