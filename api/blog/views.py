from rest_framework.viewsets import ModelViewSet
from blog.models import News
from api.blog.serializers import NewsSerializer


class NewsViewSet(ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
