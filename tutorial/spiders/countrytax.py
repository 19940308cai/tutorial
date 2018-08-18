import scrapy,os
import datetime
from tutorial.items import CountryTaxItem



class CountryTax(scrapy.Spider):
    name="countrytax"
    area="北京"
    maxPage="3215"
    taxCode="110000"
    baseUrl="http://hd.chinatax.gov.cn/fagui/action/InitCredit.do"
    proxy="http://121.69.70.182:8118"


    def start_requests(self):
        if os.path.exists("./item.txt"):
            with open("./item.txt", "r") as f:
                offset=int(f.read())
        else:
            offset=1

        for index in range(offset,int(self.maxPage)):
            with open("./item.txt","w") as f:
                 f.write(str(index))
            yield scrapy.FormRequest(meta={"proxy":self.proxy,"index":str(index)},url=self.baseUrl+"?time="+str(datetime.datetime.now().timestamp()),callback=self.run)

    def run(self,response):
        if str(response.status) == "200":
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
                scrapy.FormRequest(meta={"proxy":self.proxy,"index":response.meta['index']},url=self.baseUrl,formdata=body,method="POST",callback=self.process)
            ]
        else:
            print("方法名:run , 状态码:"+str(response.status))
            exit()

    def process(self,response):
        if str(response.status) == "200":
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
        else:
            print("方法名:process , 状态码:" + str(response.status))
            exit()

