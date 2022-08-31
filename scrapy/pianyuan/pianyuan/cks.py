import requests
from requests.cookies import RequestsCookieJar


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36',
}
url = 'https://www.xl720.com/'
res = requests.get(url, headers)
# print(res.cookies)

# 创建一个cookiejar实例
