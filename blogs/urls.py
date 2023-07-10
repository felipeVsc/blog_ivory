"""
URL configuration for blogs project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app.posts.views import *
from app.users.views import *
from app.blog.views import *

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/posts/all/<int:id>/', posts_get_all_from_blog_view.as_view()),
    path('api/posts/<int:id>/', posts_find_by_id_view.as_view()),
    path('api/posts/', posts_view.as_view()),
    path('api/posts/like/', posts_like_view.as_view()),
    path('api/posts/reply/', reply_view.as_view()),
    path('api/posts/reply/all/<int:post_id>/', reply_get_all_view.as_view()),
    path('api/posts/reply/<int:post_id>/<int:reply_id>/', reply_find_by_id_view.as_view()),
    path('api/posts/reply/like/<int:id>/', reply_get_likes_by_id_view.as_view()),
    path('api/posts/reply/like/', reply_likes_view.as_view()),
    path('api/blogs/', blogs_view.as_view()),
    path('api/blogs/<int:id>/', blogs_find_by_id_view.as_view()),
    
    path('api/author/', author_view.as_view()),

    
]
