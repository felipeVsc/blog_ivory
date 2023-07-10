from django.contrib import admin
from .models import Blog

# Register your models here.
@admin.action(description='Publish Blog')
def publish_blog(modeladmin, request, queryset):
    queryset.update(published=True)


@admin.action(description='Archive Blog')
def archive_blog(modeladmin, request, queryset):
    queryset.update(published=False)

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

    def get_queryset(self, request):
        if request.user.is_authenticated:
            return super().get_queryset(request).filter(author=request.user)

        return super().get_queryset(request).none()



admin.site.register(Blog,BlogAdmin)