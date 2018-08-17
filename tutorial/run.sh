#!/bin/bash
`scrapy crawl countrytax -a area=北京 -a maxPage=3215 -a taxCode=110000 2>/dev/null &`
