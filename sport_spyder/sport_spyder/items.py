# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from scrapy_djangoitem import DjangoItem
from scrapy.item import Field

from rest_server.models import Sports, Article


import scrapy


class SportSpyderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class ArticleItem(DjangoItem):
    # fields for this item are automatically created from the django model
    django_model = Article

class SportsItem(DjangoItem):
    # fields for this item are automatically created from the django model
    django_model = Sports