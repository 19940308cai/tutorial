# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from tutorial.items import CountryTaxItem
from tutorial.sql import Mysql

class countrytaxPipeline(object):

    def process_item(self, item, spider):
        if isinstance(item,CountryTaxItem):

            result = Mysql.insert(
                item['taxnumber'],
                item['taxname'],
                item['date'],
                item['area']
            )

            print(result)
            pass
