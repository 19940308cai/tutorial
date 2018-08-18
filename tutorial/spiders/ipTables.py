import scrapy,time
from tutorial.items import IptablesTtem



class Iptables(scrapy.Spider):
    name="iptables"
    baseUrl="http://www.xicidaili.com/nn/1"

    def start_requests(self):
        while True:
            yield scrapy.Request(url=self.baseUrl+"?z="+str(time.time()), callback=self.run)



    def run(self,response):
        trs = response.xpath("//table[@id='ip_list']/tr")
        del trs[0]
        iptablesTtem=IptablesTtem()
        for tr in trs:
            tds=tr.xpath("td")
            iptablesTtem['ip']=tds[1].xpath("text()").extract()[0]
            iptablesTtem['port']=tds[2].xpath("text()").extract()[0]
            iptablesTtem['address']="无" if not tds[3].xpath("a/text()").extract() else tds[3].xpath("a/text()").extract()[0]
            iptablesTtem['type']=tds[4].xpath("text()").extract()[0]
            iptablesTtem['schema']=tds[5].xpath("text()").extract()[0]
            yield iptablesTtem