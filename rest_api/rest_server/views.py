import http

from rest_framework.generics import ListAPIView
from .serializers import ArticleSerializer, SportsSerializer
from .models import Article, Sports, objects
from datetime import datetime
from .services import BadRequest, NoContent, PaginationArticles, ArticleFilter
from rest_framework.exceptions import NotFound, APIException
from django.core.exceptions import BadRequest
from django_filters.rest_framework import DjangoFilterBackend

class ArticlesViewFilter(ListAPIView):

    """Sport events news feed with backend filter by sport type"""

    serializer_class = ArticleSerializer
    filter_backends = (DjangoFilterBackend,)
    pagination_class = PaginationArticles
    filterset_class = ArticleFilter

    def get_queryset(self):
        queryset = Article.objects.all()
        return queryset


class ArticlesView(ListAPIView):

    """Sport events news feed with pagination facility"""


    serializer_class = ArticleSerializer
    pagination_class = PaginationArticles

    def get_queryset(self):
        queryset = Article.objects.all()
        return queryset

    def get_sport(self, sport_name):
        sport_name = sport_name.lower().capitalize()
        sport_inst = Sports.objects.filter(name=sport_name).first()
        if sport_inst:
            return sport_inst
        else:
            return None

    def get_queryset(self):
        sport_inst = self.get_sport(self.kwargs['name'])
        if sport_inst:
            queryset = Article.objects.filter(name=sport_inst.id).all()
            return queryset
        else:
            raise NotFound(f"Couldn't find this kind of sport: {self.kwargs['name']}")



class SportsView(ListAPIView):

    """List of available sport types"""

    serializer_class = SportsSerializer


    def get_queryset(self):
        sports = Sports.objects.all()
        return sports


class ArticlesFreshView(ArticlesView):

    """Sport events news feed with last update check"""

    serializer_class = ArticleSerializer

    def convert_naive_to_aware_date(self, date_to_convert, sport_inst):
        timezone = sport_inst.last_modified.tzinfo
        try:
            date_to_return = datetime.strptime(date_to_convert, '%Y-%m-%d %H:%M:%S').replace(tzinfo=timezone)
            return date_to_return
        except Exception as e:
            return None

    def get_queryset(self):
        sport_inst = self.get_sport(self.kwargs['name'])
        if sport_inst:
            lastupdate = self.convert_naive_to_aware_date(self.kwargs['lastupdate'], sport_inst)
            if lastupdate:
                if sport_inst.last_modified > lastupdate:
                    queryset = Article.objects.filter(name=sport_inst.id).all()
                    return queryset
                else:
                    raise NoContent("Don't have so fresh data")
            else:
                raise BadRequest('Invalid date format. Should be YYYY-mm--dd HH:MM:SS')
        else:
            raise NotFound(f"Couldn't find this kind of sport: {self.kwargs['name']}")
