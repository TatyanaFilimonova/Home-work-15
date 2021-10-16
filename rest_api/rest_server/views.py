import http

from rest_framework.generics import ListAPIView, GenericAPIView
from .serializers import ArticleSerializer, SportsSerializer
from .models import Article, Sports, objects
from datetime import datetime
from rest_framework.response import Response
from .services import PaginationArticles
from rest_framework.exceptions import NotFound, APIException
from django.core.exceptions import BadRequest
from rest_framework import status

class NoContent(APIException):
    status_code = status.HTTP_204_NO_CONTENT
    default_detail = ('No content by your request')
    default_code = 'no_content'



class ArticlesView(ListAPIView):
    serializer_class = ArticleSerializer
    pagination_class = PaginationArticles

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

    serializer_class = SportsSerializer

    def get_queryset(self):
        sports = Sports.objects.all()
        return sports


class ArticlesFreshView(ArticlesView):
    serializer_class = ArticleSerializer
    pagination_class = PaginationArticles

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
                raise NotFound('Invalid date format. Should be YYYY-mm--dd HH:MM:SS')
        else:
            raise NotFound(f"Couldn't find this kind of sport: {self.kwargs['name']}")
