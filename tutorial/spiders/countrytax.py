import scrapy,os,time
import datetime
from tutorial.items import CountryTaxItem



class CountryTax(scrapy.Spider):
    name="countrytax"
    area="北京"
    maxPage="3215"
    taxCode="110000"
    baseUrl="http://hd.chinatax.gov.cn/fagui/action/InitCredit.do"

    headers = {'Host': 'hd.chinatax.gov.cn', 'Proxy-Connection': 'keep-alive',}

    #种cookie
    def start_requests(self):
        yield scrapy.FormRequest(
                url=self.baseUrl,
                headers=self.headers,
                callback=self.parse
            )

    #拿cookie去访问首页
    def parse(self, response):
        print(response.headers)
        for index in range(0,1):
            yield scrapy.Request(
                    url=self.baseUrl+"?timestap="+str(time.time()),
                    headers=self.headers,
                    meta={"cPage":str(index)},
                    callback=self.run
                )

    #迭代去操作业务
    def run(self,response):
        if response.status == 200:
            try:
                randcode = response.selector.xpath('//input[@name="randCode"]/@value').extract()[0]
            except Exception as e:
                with open("run_error.html","wb") as f:
                    f.write(response.body)
                print("方法名:run , 状态码:" + str(response.status) + e.__str__())
                return
            body = {
                "articleField01" : "",
                "articleField02": "",
                "articleField03": "2017",
                "cPage":response.meta['cPage'],
                "articleField06": "",
                "randCode":randcode,
                "flag":"1",
                "scount":"2",
                "taxCode":self.taxCode
            }
            return [ scrapy.FormRequest(
                url=self.baseUrl,
                formdata=body,
                headers=self.headers,
                method="POST",
                callback=self.process)]
        else:
            print("方法名:run , 状态码:"+str(response.status))
            return

    def process(self,response):
        if response.status == 200:
            try:
                trs=response.selector.xpath('//td[@class="sv_hei"]/table/tr')
                countrytax = CountryTaxItem()
                for key, value in enumerate(trs):
                    if key == 0 or len(trs) - 1 == key:
                        continue
                    tds = value.xpath('td/text()')
                    countrytax['taxnumber'] = str(tds[0].extract())
                    countrytax['taxname'] = str(tds[1].extract())
                    countrytax['date'] = str(tds[2].extract())
                    countrytax['area'] = self.area
                    yield countrytax
            except Exception as e:
                print("方法名:process , 状态码:" + str(response.status)+e.__str__())
                return
        else:
            print("方法名:process , 状态码:" + str(response.status))
            return

