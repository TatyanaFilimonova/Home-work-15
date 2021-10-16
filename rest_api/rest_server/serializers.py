from rest_framework import serializers
from .models import Article, Sports

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        exclude = ['id', 'name']


class SportsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sports
        exclude = ['id']