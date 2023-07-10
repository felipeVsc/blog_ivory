from django.contrib import admin
from .models import Blog
from django import forms
from django.contrib.auth.models import User
# Register your models here.

@admin.action(description='Publish Blog')
def publish_blog(modeladmin, request, queryset):
    queryset.update(published=True)


@admin.action(description='Archive Blog')
def archive_blog(modeladmin, request, queryset):
    queryset.update(published=False)

class BlogForm(forms.ModelForm):
    def __init__(self,*args, **kwargs):
        super(BlogForm, self).__init__(*args, **kwargs)
        self.fields['author'].queryset = User.objects.filter(username=self.user)

class BlogAdmin(admin.ModelAdmin):
    actions = [
        publish_blog,
        archive_blog
    ]

    list_display = [
        "active",
        "name",
        "created_at"
    ]

    exclude = ['created_at']

    form = BlogForm
    def get_form(self, request, obj=None, **kwargs):
        kwargs["form"] = BlogForm
        form = super().get_form(request, obj, **kwargs)
        form.user = request.user
        return form
  
    def get_queryset(self, request):
        if request.user.is_authenticated:
            return super().get_queryset(request).filter(author=request.user)

        return super().get_queryset(request).none()

admin.site.register(Blog,BlogAdmin)