# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from tutorial.items import CountryTaxItem
from tutorial.items import IptablesTtem
from tutorial.model.countryTax import countryTax
from tutorial.model.iptable import iptable
from scrapy import log

class productPipeline(object):

    def process_item(self, item, spider):


        if isinstance(item,CountryTaxItem):
            m_countryTax = countryTax()
            result = m_countryTax.selectOneDataByCondition([
                ['articleField01','=',item['articleField01']],
                ['articleField02', '=', item['articleField02']],
                ['articleField03', '=', item['articleField03']],
                ['articleField06', '=', item['articleField06']],
                ['cPage', '=', item['cPage']],
                ['randCode', '=', item['randCode']],
                ['flag', '=', item['flag']],
                ['scount', '=', item['scount']],
                ['taxCode', '=', item['taxCode']],
            ])
            if not result:
                m_countryTax.insert(item)


        if isinstance(item,IptablesTtem):
            m_iptable = iptable()
            result = m_iptable.selectOneDataByCondition([
                ['port','=',item['port']],
                ['address', '=', item['address']],
                ['type', '=', item['type']],
                ['schema', '=', item['schema']],
            ])
            if not result:
                m_iptable.insert(item)

