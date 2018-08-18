import scrapy,time,random
from tutorial.model.iptable import iptable



class localtest(scrapy.Spider):
    name="localtest"
    baseUrl="http://47.92.119.35/service/window/index"


    def start_requests(self):
        m_iptable = iptable()
        list = m_iptable.selectAllDataByCondition(condition=[['use', '=', '0']], limit=[20])
        for index in range(0,10):
            rand = random.randint(0, 19)
            schema = list[rand][2].lower()
            domain = list[rand][1]
            port   = list[rand][3]
            # url = schema + "://" + domain+":"+port
            proxy = "http://121.69.70.182:8118"
            yield scrapy.Request(url=self.baseUrl+"?z="+str(time.time()),meta={"index":index,"proxy":proxy}, callback=self.run)



    def run(self,response):
        with open("demo_"+str(response.meta['index'])+".html","wb") as f:
            f.write(response.body)