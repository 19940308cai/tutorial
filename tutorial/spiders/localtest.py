import scrapy,time,random
from tutorial.model.iptable import iptable



class localtest(scrapy.Spider):
    name="localtest"
    baseUrl="http://47.92.119.35/service/window/index"


    def start_requests(self):
        yield scrapy.Request(url=self.baseUrl + "?z=" + str(time.time()), meta={"index": 1},
                             callback=self.run)


    def run(self,response):
        with open("demo_"+str(response.meta['index'])+".html","wb") as f:
            f.write(response.body)
        yield scrapy.Request(url=self.baseUrl + "?z=" + str(time.time()), meta={"index": 33333},
                             callback=self.demo)

    def demo(self,response):
        with open("demo_"+str(response.meta['index'])+".html","wb") as f:
            f.write(response.body)