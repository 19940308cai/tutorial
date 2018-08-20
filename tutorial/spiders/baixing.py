import scrapy,time
# from tutorial.items import IptablesTtem



class Baixing(scrapy.Spider):
    name="baixing"
    baseUrl="http://beijing.baixing.com/"
    def start_requests(self):
        yield scrapy.Request(url=self.baseUrl, callback=self.run)
        # for i in range(1,10):
        #     yield scrapy.Request(url=self.baseUrl+str(i),callback=self.run)



    def run(self,response):
        with open("./demo.html","wb") as f:
            f.write(response.body)
        yield scrapy.Request(url=self.baseUrl+"?time=1", callback=self.run)