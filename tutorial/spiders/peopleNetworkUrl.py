import scrapy
import datetime,os
from tutorial.items import CountryTaxItem



class PeopleNetworkUrl(scrapy.Spider):
    name="peopleNetwork"
    baseUrl="http://beijing.baixing.com/gongzuo/?src=topbar"

    def __init__(self,area=None,maxPage=None,taxCode=None,*args,**kwargs):
        super(PeopleNetworkUrl,self).__init__(*args,**kwargs)


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


