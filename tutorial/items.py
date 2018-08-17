

# Define here the models for your scraped items
#
# See documentation in=scrapy.Field()
# https=scrapy.Field()//doc.scrapy.org/en/latest/topics/items.html

import scrapy

#城市实体
class CountryTaxItem(scrapy.Item):
    taxnumber =scrapy.Field()
    taxname  = scrapy.Field()
    date = scrapy.Field()
    area = scrapy.Field()


