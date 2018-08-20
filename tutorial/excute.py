from scrapy.cmdline import execute

# execute(['scrapy','crawl','iptables']) #900s
# execute(['scrapy','crawl','localtest'])
# execute(['scrapy','crawl','countrytax']) #30s请求一次
execute(['scrapy','crawl','baixing']) #300s请求一次
# --logfile=log/iptables.log


