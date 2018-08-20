# import requests
#
#
# response = requests.post("http://47.92.119.35/service/window/index", proxies={"protocol":"http://125.117.134.169:9000"}, timeout=2)
#
# print(response.content)
#


import re
data = ['上一页', '1', '2', '3', '44', '45', '46', '47', '49', '50', '51', '52', '99', '100', '下一页']
print(data[len(data)-1])
exit()

str="/gongren/m37318?src=subCategory"
data = re.findall("^(/gongren/.+)\?(.+)",str)
print(data[0][0])