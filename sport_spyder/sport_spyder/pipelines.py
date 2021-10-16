# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import datetime
from django.db import transaction
from itemadapter import ItemAdapter
import re
from .spiders.tennis import *
from rest_server.models import Sports, Article


class SportSpyderClearText:
    def del_new_lines_and_spaces(self, element):
        element = re.sub('\n', '', element)
        element = element.strip()
        return element

    def del_single_quotes(self, element):
        element = re.sub("\'", "'", element)
        return element

    def change_new_line(self, element):
        element = re.sub("\n", "\\n", element)
        return element

    def del_xa(self, element):
        element = re.sub("\xa0", " ", element)
        return element

    def process_item(self, item, spider):
        adapter = ItemAdapter(item)
        adapter['header'] = self.del_new_lines_and_spaces(adapter['header'])
        adapter['post_date'] = self.del_new_lines_and_spaces(adapter['post_date'])
        adapter['short_text'] = self.del_new_lines_and_spaces(adapter['short_text'])
        adapter['short_text'] = self.del_xa(adapter['short_text'])
        adapter['tourney'] = self.del_new_lines_and_spaces(adapter['tourney'])
        adapter['full_text'] = self.del_single_quotes(adapter['full_text'])
        adapter['full_text'] = self.del_xa(adapter['full_text'])
        adapter['full_text'] = self.change_new_line(adapter['full_text'])
        return item


class SportSpyderSaveToDB:

    @transaction.atomic
    def open_spider(self, spider):
        self.sid = transaction.savepoint()
        sport = Sports.objects.filter(name=spider.name).first()
        if sport:
            Sports.objects.filter(name=spider.name).update(last_modified=datetime.now())
            Article.objects.filter(name=sport).all().delete()
        else:
            sport = Sports(name=spider.name)
            sport.save()

    def close_spider(self, spider):
        transaction.savepoint_commit(self.sid)

    def process_item(self, item, spider):
        adapter = ItemAdapter(item)
        sport = Sports.objects.filter(name=spider.name).first()
        article = Article(
            name=sport,
            header=adapter['header'],
            short_text=adapter['short_text'],
            tourney=adapter['tourney'],
            full_text=adapter['full_text'],
            author=adapter['author'],
            post_date=adapter['post_date'],
            source=adapter['source']
        )
        article.save()
        return item

class SportSpyderClearDate:
    def process_item(self, item, spider):
        adapter = ItemAdapter(item)
        adapter['post_date'] = re.sub('Published[\w\W]+, ', '', adapter['post_date'])
        date_ = datetime.strptime(adapter['post_date'], '%d %b %Y')
        adapter['post_date'] = date_.strftime("%d %B, %Y")
        return item
