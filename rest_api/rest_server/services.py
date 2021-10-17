from .models import Article, Sports
from rest_framework.pagination import PageNumberPagination
from django_filters import rest_framework as filters
from rest_framework.exceptions import APIException
from rest_framework import status


class NoContent(APIException):
    status_code = status.HTTP_204_NO_CONTENT
    default_detail = ('No content by your request')
    default_code = 'no_content'


class BadRequest(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = ('Bad request')
    default_code = 'bad_request'


class ArticleFilter(filters.FilterSet):
    name__name = filters.CharFilter()

    class Meta:
        model = Article
        fields = ['name__name']


class PaginationArticles(PageNumberPagination):
    page_size = 2
    max_page_size = 5