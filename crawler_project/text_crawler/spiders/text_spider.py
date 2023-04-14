import scrapy
import trafilatura
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor
from ..items import PageContentItem

class textSpider(scrapy.Spider):
    name= "pageContentCrawler"
    allowed_domains=['en.wikipedia.org']
    start_urls =[
        'https://en.wikipedia.org/wiki/Musk_family'
    ]
    rules= [Rule(
        LinkExtractor(allow=allowed_domains), 
                 callback= 'parse', follow=True)]
    
    def parse(self, response):
        items= PageContentItem()
        print(response)
        fullText=trafilatura.extract(response.text)
        title= response.css("head title::text").extract()
        items['page_url']=response.url
        items['page_title']=title
        items['page_content']= fullText
        yield items



      
        