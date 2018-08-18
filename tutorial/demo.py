import requests


response = requests.post("http://47.92.119.35/service/window/index", proxies={"protocol":"http://125.117.134.169:9000"}, timeout=2)

print(response.content)