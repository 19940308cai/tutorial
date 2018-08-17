import scrapy
import datetime,os
from tutorial.items import CountryTaxItem



class CountryTax(scrapy.Spider):
    name="countrytax"
    baseUrl="http://hd.chinatax.gov.cn/fagui/action/InitCredit.do"



    def __init__(self,area=None,maxPage=None,taxCode=None,*args,**kwargs):
        super(CountryTax,self).__init__(*args,**kwargs)
        self.area=area
        self.maxPage=maxPage
        self.taxCode=taxCode

    def start_requests(self):
       if os.path.exists("./item.txt") :
            with open("./item.txt","r") as f:
                offset=f.read()
       else:
            offset=1

       for index in range(int(offset),int(self.maxPage)):
            with open("./item.txt","w") as f:
                 f.write(str(index))
            yield scrapy.FormRequest(meta={"index":str(index)},url=self.baseUrl+"?time="+str(datetime.datetime.now().timestamp()),callback=self.run)
       os.remove("./item.txt")

    def run(self,response):
        body = {}
        body['articleField01'] = ""
        body['articleField02'] = ""
        body['articleField03'] = "2017"
        body['articleField06'] = ""
        body['cPage']   = response.meta['index']
        body['randCode']= response.selector.xpath('//input[@name="randCode"]/@value').extract()[0]
        body['flag']   = "1"
        body['scount'] ="0"
        body['taxCode']=self.taxCode
        return [
            scrapy.FormRequest(meta={"index":response.meta['index']},url=self.baseUrl,formdata=body,method="POST",callback=self.process)
        ]


    def process(self,response):
        trs=response.selector.xpath('//td[@class="sv_hei"]/table/tr')
        countrytax = CountryTaxItem()
        for key,value in enumerate(trs):
            if key == 0 or len(trs)-1 == key:
                continue
            tds=value.xpath('td/text()')
            countrytax['taxnumber'] = str(tds[0].extract())
            countrytax['taxname']   = str(tds[1].extract())
            countrytax['date']      = str(tds[2].extract())
            countrytax['area']      = self.area
            yield countrytax


