#!/bin/bash

. absolutepath.sh

`scrapy crawl iptables --logfile=log/iptables.log`
