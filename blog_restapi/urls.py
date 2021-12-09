"""blog_restapi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path, include
from blog.views import index, ViewNews,  register, CreateNews, profile, choise_category, delete_news, edit_news

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='home'),
    path('news/<int:pk>/', ViewNews.as_view(), name='view_news'),
    path('add-news/', CreateNews.as_view(), name='add_news'),
    path('accounts/register/', register, name='register'),
    path('accounts/profile/', profile, name='profile'),
    path('category_choise/<name>/', choise_category, name='choise_category'),
    path('delete_news/<news_pk>/', delete_news, name='delete_news'),
    path('edit_news/<news_pk>/', edit_news, name='edit_news'),
]


urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),

]
