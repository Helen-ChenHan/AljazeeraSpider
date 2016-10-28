import scrapy
import re
import os.path
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.selector import HtmlXPathSelector
from craigslist_sample.items import ALJItem
from scrapy.utils.response import body_or_str

class MySpider(CrawlSpider):
    name = "alj"
    allowed_domains = ["aljazeera.com"]
    start_urls = ['http://www.aljazeera.com/']

    base_url = 'http://www.aljazeera.com/xml/sitemaps/sitemap_'
    year = ['2016_A','2015','2014','2013','2012','2011','2010','2009','2008','2007','2006','2005','2004','2003']

    def parse(self,response):
        for y in self.year:
            url = self.base_url+y+'.xml'
            yield scrapy.Request(url,self.parseList)

    def parseList(self,response):
        nodename = 'loc'
        text = body_or_str(response)
        r = re.compile(r"(<%s[\s>])(.*?)(</%s>)" % (nodename, nodename), re.DOTALL)
        for match in r.finditer(text):
            url = match.group(2)
            yield scrapy.Request(url,self.parse_items)

    def parse_items(self, response):
        hxs = HtmlXPathSelector(response)
        items = []
        item = ALJItem()
        item["title"] = hxs.select('//h1[@class="heading-story"]/text()').extract()[0]
        article = hxs.select('string(//div[contains(@class,"article-body") or contains(@class ,"article-body-full")])').extract()
        item["article"] = "\n".join(article).encode('utf8')
        item['link'] = response.url
        item['date'] = hxs.select('//time/text()').extract()[0].encode('utf-8')
        items.append(item)

        return(items)