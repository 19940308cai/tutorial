import scrapy,time



class localtest(scrapy.Spider):
    name="localtest"
    baseUrl="http://47.92.119.35/service/window/index"

    def start_requests(self):

        for index in range(0,20):
            yield scrapy.Request(
                             url=self.baseUrl + "?z="+str(time.time())+"&flag="+str(index),
                             meta={"index": str(index)},
                             callback=self.run)



    def run(self,response):
        yield scrapy.Request(
                             url=self.baseUrl + "?t="+str(time.time())+"&father="+str(response.meta['index']),
                             meta={"index":str(response.meta['index'])+"_1","proxy":response.meta['proxy']},
                             callback=self.demo)

    def demo(self,response):
        with open("demo_"+str(response.meta['index'])+".html","wb") as f:
            f.write(response.body)