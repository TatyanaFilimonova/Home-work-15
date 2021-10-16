import scrapy
import re
from datetime import datetime


class TennisSpider(scrapy.Spider):
    name = 'Tennis'
    allowed_domains = ['www.wtatennis.com']
    start_urls = ['https://www.wtatennis.com/news/']
    custom_settings = {
        'ITEM_PIPELINES': {
            'sport_spyder.pipelines.SportSpyderClearText': 100,
            'sport_spyder.pipelines.SportSpyderSaveToDB': 300,
        }
    }

    def parse(self, response):
        links = response.xpath("//article[contains(@class, 'media-thumbnail')]/a/@href").extract()
        for link in links[:2]:
            yield scrapy.Request(url=re.sub('/news/', '', self.start_urls[0]) + link)

        for content in response.xpath("//article[@class = 'article widget']"):
            text_lst = []
            for p_ in content.xpath("div[1]/p"):
                bold = p_.xpath("strong/text()").get()
                text = p_.xpath("text()").get()
                if bold:
                    if text:
                        text_lst.append('\n'+bold+'\n'+text)
                else:
                    if text:
                        text_lst.append('\n' + text)
            article_date_head = content.xpath("//time[@class = 'content-page-header__date']/text()").extract()
            article_date_tail = content.xpath("//time[@class = 'content-page-header__date']/span/text()").get()
            if article_date_tail is None:
                article_date = datetime.today().strftime("%d %B, %Y")
            elif re.search(r'ago', article_date_tail):
                article_date = datetime.today().strftime("%d %B, %Y")
            else:
                if len(article_date_head)>1:
                    article_date = article_date_head[1] + article_date_tail
                else:
                    article_date = article_date_head[0] + article_date_tail
            yield{
                "header": content.xpath("//h1[contains(@class, 'content-page-header')]/text()").get(),
                "short_text": content.xpath("//p[@class ='content-page-header__summary']/text()").get(),
                "full_text": "".join(text_lst),
                "tourney":  content.xpath("//div[@class='content-page-header__meta']/span/text()").get(),
                "author": content.xpath("//p[@class = 'content-page-header__author']/span/text()").get(),
                "post_date": article_date,
                "source": response.request.url
            }
