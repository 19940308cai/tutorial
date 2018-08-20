import scrapy,time
from tutorial.items import IptablesTtem



class Iptables(scrapy.Spider):
    name="iptables"
    baseUrl="http://www.xicidaili.com/wt/"
    def start_requests(self):
        index=1
        while True:
            yield scrapy.Request(url=self.baseUrl+str(index)+"?z="+str(time.time()),callback=self.run)
            index+=1
            time.sleep(500)


    def run(self,response):
        if response.status == 200:
            trs = response.xpath("//table[@id='ip_list']/tr")
            del trs[0]
            iptablesTtem=IptablesTtem()
            for tr in trs:
                tds=tr.xpath("td")
                iptablesTtem['ip']=tds[1].xpath("text()").extract()[0]
                iptablesTtem['port']=tds[2].xpath("text()").extract()[0]
                iptablesTtem['address']="无" if not tds[3].xpath("a/text()").extract() else tds[3].xpath("a/text()").extract()[0]
                iptablesTtem['type']=tds[4].xpath("text()").extract()[0]
                iptablesTtem['schema']=tds[5].xpath("text()").extract()[0].lower()
                print(iptablesTtem)
                yield iptablesTtem