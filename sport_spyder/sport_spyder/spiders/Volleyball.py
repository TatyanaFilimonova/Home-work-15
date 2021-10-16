import scrapy
import re


class VolleyballSpider(scrapy.Spider):
    name = 'Volleyball'
    allowed_domains = ['en.volleyballworld.com']
    start_urls = ['https://en.volleyballworld.com/volleyball/competitions/vnl-2021/news/']
    custom_settings = {
            'ITEM_PIPELINES': {
                'sport_spyder.pipelines.SportSpyderClearDate': 200,
                'sport_spyder.pipelines.SportSpyderSaveToDB': 300,
            }
    }

    def parse(self, response):
        links = response.xpath(
         "//section[@class='d3-l-grid--outer d3-l-" +
         "section-row d3-c-editorial-list fivb-addons-editorial-list']//a/@href").extract()
        for link in links:
            yield scrapy.Request(url=self.start_urls[0] + re.sub('/volleyball/competitions/vnl-2021/news/', '', link))
        for content in response.xpath("//article[@class = 'd3-l-section-row oc-c-article fivb-addons-story']"):
            text_lst = []
            for text in content.xpath("//div[@class = 'oc-c-body-part oc-c-markdown-stories']/p/text()").extract():
                text_lst.append(text+'\n')
            regex = r"competitions\/(?P<tour>[\w\W\-]+)\/news\/"
            match = re.search(regex, self.start_urls[0])
            if match:
                tour = match.group('tour')
            else:
                tour = ''
            yield {
                "header": content.xpath("//h1[@class='oc-c-article__title']/text()").get(),
                "short_text": content.xpath("//p[@class = 'oc-c-article__summary']/text()").get(),
                "full_text": "".join(text_lst),
                "tourney": tour,
                "author": '',
                "post_date": content.xpath("//div[@class='oc-c-article__date']/p/text()").get(),
                "source": response.request.url

            }
