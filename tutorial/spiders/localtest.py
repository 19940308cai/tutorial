import scrapy,time



class localtest(scrapy.Spider):
    name="localtest"
    baseUrl="http://httpbin.org/get"

    def start_requests(self):
        for index in range(0,2):
            yield scrapy.Request(
                             url=self.baseUrl + "?z=" + str(index),
                             meta={"index": str(index)},
                             callback=self.run)


    def run(self,response):
        print(response.text)
        yield scrapy.Request(
                             url=self.baseUrl + "?z="+str(time.time()),
                             meta={"index":str(response.meta['index'])+"_1","proxy":response.meta['proxy']},
                             callback=self.demo)

    def demo(self,response):
        with open("demo_"+str(response.meta['index'])+".html","wb") as f:
            f.write(response.body)