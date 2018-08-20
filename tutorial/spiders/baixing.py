import scrapy,re,time

from tutorial.items import JobCategory



class Baixing(scrapy.Spider):
    name="baixing"
    baseUrl="http://beijing.baixing.com/gongzuo/?src=topbar"
    prefixUrl="http://beijing.baixing.com"
    def start_requests(self):
        yield scrapy.Request(url=self.baseUrl, callback=self.run)
        # for i in range(1,10):
        #     yield scrapy.Request(url=self.baseUrl+str(i),callback=self.run)



    def run(self,response):
       if response.status == 200:
           lis = response.xpath("//li[@class='nav-item']")
           for li in lis:
                dl=li.xpath("dl")
                dds=dl.xpath("dd")
                for dd in dds:
                # dd = dds[0]
                    #一级分类:列表页面路由
                    a_title=dd.xpath("a/text()").extract()[0]
                    a_href = dd.xpath("a/@href").extract()[0]
                    href=re.findall("^(/\w+/.+)\?(.+)", a_href)
                    #请求工作列表页面
                    '''
                    page:当前请求页数
                    end:探分页总数是否结束 0-没结束 1-结束
                    '''
                    yield scrapy.Request(
                        url=self.prefixUrl+href[0][0]+"/?page=1",
                        meta={"url":self.prefixUrl+href[0][0]+"/","page":1,"end":0},
                        callback=self.process,
                    )
                # break


    def process(self,response):
        if response.meta['end'] == 0 :
            #获取当前页面的最大值
            ul=response.xpath('//ul[@class="list-pagination"]')
            lis = ul.xpath('li')
            #装在分页
            lisq= []
            for li in lis:
                if li.xpath('a/text()').extract():
                    title = li.xpath('a/text()').extract()[0]
                    lisq.append(title)

            '''
            该网站对于分页有2种规律
            1.如当前页为最大页面，则无下一页,也就是当前页的下标为 len(lisq)-1
            2.如果当前页面不是最大页，则有下一页按钮，最大值为 len(lisq)-2
            '''
            print(lisq)
            if lisq[len(lisq)-1] == "下一页":
                print("还没有拿到最大值，可以继续往下面挖")
                yield scrapy.Request(
                    url=response.meta['url']+"?page="+str(lisq[len(lisq)-2]),
                    meta={"url":response.meta['url'],"page": int(lisq[len(lisq)-2]), "end": 0},
                    callback=self.process,
                )
            else:
                print("这个值已经是最大值了,可以查数据了")
                for index in range(1,int(lisq[len(lisq)-1])):
                # for index in range(1, 3):
                    yield scrapy.Request(
                        url=response.meta['url']+"?page="+str(index)+"&t="+str(time.time()),
                        callback=self.endProcess,
                    )



    def endProcess(self,response):
        JobCategoryItem = JobCategory()
        # 具体的职位单元
        jobs = response.xpath("//li[@class='listing-ad table-view-item apply-item  item-pinned']")
        for job in jobs:
            a = job.xpath("div[@class='table-view-body job-list']/div[@class='preview-hover']/a[@class='ad-title']")
            # 当前当前页面的该个工种塞入数据库.
            JobCategoryItem['jobtitle'] = a.xpath("text()").extract()[0]
            JobCategoryItem['jobhref'] = a.xpath("@href").extract()[0]
            yield JobCategoryItem