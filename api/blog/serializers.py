# from rest_framework import serializers
#
#
# class NewsSerializer(serializers.Serializer):
#     author = serializers.CharField()
#     title = serializers.CharField(max_length=100)
#     content = serializers.CharField()
#     photo = serializers.ImageField()
#     created_at = serializers.DateTimeField(read_only=True)
#     updated_at = serializers.DateTimeField(read_only=True)
#     category = serializers.CharField()


from rest_framework.serializers import ModelSerializer
from blog.models import News


class NewsSerializer(ModelSerializer):
    class Meta:
        model = News
        #fields = ['title']
        fields = '__all__'
