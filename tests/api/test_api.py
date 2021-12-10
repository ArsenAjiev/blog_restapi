import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from django.contrib.auth.models import User
from api.blog.serializers import NewsSerializer
from datetime import datetime

from blog.models import News, Category


@pytest.mark.django_db
class TestPostsApi:
    def setup_method(self):
        self.client = APIClient()
        self.url = reverse("api:news-list")
        self.user = User.objects.create_user(username='test_user', email='test_email', password='test_password')
        self.category = Category.objects.create(title='Sport')
        self.news1 = News.objects.create(title='title 1', content='content 1', author=self.user, category=self.category, created_at='01.01.2021', updated_at='01.02.2021' )
        self.news2 = News.objects.create(title='title 2', content='content 2', author=self.user, category=self.category,
                                         created_at='01.01.2021', updated_at='01.02.2021')


# проверка соединения
    def test_status_api(self):
        response = self.client.get(self.url)
        assert response.status_code == status.HTTP_200_OK


# проверка получения данных
# в serializer_data сначала news2 а затем news1 из за сортировки по дате!

    def test_get(self):
        response = self.client.get(self.url)
        serializer_data = NewsSerializer([self.news2, self.news1], many=True).data
        assert serializer_data == response.data
