# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from tutorial.items import CountryTaxItem
from tutorial.items import IptablesTtem
from tutorial.model.countryTax import countryTax
from tutorial.model.iptable import iptable

class productPipeline(object):

    def process_item(self, item, spider):


        if isinstance(item,CountryTaxItem):
            m_countryTax = countryTax()
            result = m_countryTax.selectOneDataByCondition([
                ['taxnumber', '=', item['taxnumber']],
                ['taxname', '=', item['taxname']],
                ['date', '=', item['date']],
                ['area', '=', item['area']],
            ])
            if result is None:
                m_countryTax.insert(item)




        if isinstance(item,IptablesTtem):
            m_iptable = iptable()
            result = m_iptable.selectOneDataByCondition([
                ['port','=',item['port']],
                ['address', '=', item['address']],
                ['type', '=', item['type']],
                ['schema', '=', item['schema']],
            ])
            if result is None:
                m_iptable.insert(item)

