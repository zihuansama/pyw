import scrapy
import items
from items import PianyuanItem
import chaojiying
import time

from selenium import webdriver
from chaojiying import Chaojiying_Client
from selenium.webdriver.common.by import By
import requests
# https://www.pianyuan.org/mv?p=1
# https://www.pianyuan.org/mv?p=2
# https://www.pianyuan.org/mv?p=3
# Cookies [{'domain': '.pianyuan.org', 'expiry': 1661795285, 'httpOnly': False, 'name': '_gat_gtag_UA_136876477_4', 'path': '/', 'secure': False, 'value': '1'},
#          {'domain': '.pianyuan.org', 'expiry': 1661881625, 'httpOnly': False, 'name': '_gid', 'path': '/', 'secure': False, 'value': 'GA1.2.61497281.1661795225'},
#          {'domain': '.pianyuan.org', 'expiry': 1696355225, 'httpOnly': False, 'name': '_ga', 'path': '/', 'secure': False, 'value': 'GA1.2.1018373145.1661795225'},
#          {'domain': 'www.pianyuan.org', 'httpOnly': False, 'name': 'PHPSESSID', 'path': '/', 'secure': False, 'value': '2gmo5q56390r2em2jf422c74a2'},
#          {'domain': 'www.pianyuan.org', 'expiry': 1662083224, 'httpOnly': True, 'name': 'security_session_verify', 'path': '/', 'secure': False, 'value': '3d9b3d32515920f60ac5bf5d4bea0ea6'}]
# def parse_headers():
#     h = """Accept: application/json, text/javascript, */*; q=0.01
#       Accept-Encoding: gzip, deflate, br
#       Accept-Language: zh-CN,zh;q=0.9
#       Cookie:_ga=GA1.2.1458076932.1658338284; _gid=GA1.2.1064155033.1661778096; PHPSESSID=d5ivgr3dqjbimglaq65eqmpql0; py_loginauth=WyI2OTQyNTg2OTJAcXEuY29tIiwxNjYxNzkzMTc3LCJmZTg5ZjU3MTkzYzJjODM0Il0%3D; security_session_verify=434b1776d9aa3516f7a280ab65a3642e
#       Host: www.pianyuan.org
#       Referer: https://www.pianyuan.org/
#       User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"""
#     headers = {}
#     for i in (i.strip() for i in h.split("\n")):
#         k, v = i.split(":", 1)[0], i.split(":", 1)[1]
#         headers[k] = v.strip()
#
#     return headers


class PianyuanSpiderSpider(scrapy.Spider):
    name = 'pianyuan_spider'
    allowed_domains = ['pianyuan.org']
    start_urls = ['https://pianyuan.org']
    # # headers = parse_headers()
    #
    # # src=allowed_domains+//div[@class="litpic"]/a/img/@src
    # title=//div[@class="litpic"]/a/@title
    def getCookie(self):
        driver = webdriver.Chrome()
        base_url = 'https://www.pianyuan.org/User/login.html'
        index_url = 'https://www.pianyuan.org/?p=1'
        driver.get(base_url)
        img = driver.find_element(By.XPATH, '/html/body/div[2]/div/section/div/form/div[4]/div/img').screenshot_as_png
        chaojiying = Chaojiying_Client('zihuansama', '123456', '938191')
        dic = chaojiying.PostPic(img, 1005)
        verifyimg = dic['pic_str']
        USERNAME = '694258692@qq.com'
        PASSWORD = 'w526079.'
        driver.find_element(By.XPATH, '/html/body/div[2]/div/section/div/form/div[1]/div/input').send_keys(USERNAME)
        driver.find_element(By.XPATH, '/html/body/div[2]/div/section/div/form/div[2]/div/input').send_keys(PASSWORD)
        driver.find_element(By.XPATH, '/html/body/div[2]/div/section/div/form/div[3]/div/input').send_keys(verifyimg)
        time.sleep(3)
        driver.find_element(By.XPATH, '/html/body/div[2]/div/section/div/form/div[6]/div/button').click()
        time.sleep(3)

        # cookies = driver.get_cookies()
        # print('Cookies', cookies)
        # driver.close()
        #
        # # set cookies to requests
        # session = requests.Session()
        # for cookie in cookies:
        #     session.cookies.set(cookie['name'], cookie['value'])

        # response_index = session.get(index_url)
        temp = []
        for i in driver.get_cookies():
            temp.append(i['name'] + "=" + i['value'])
        # 返回字符串cookie
        return ';'.join(temp)

    def parse(self, response):

        a_list = response.xpath('//div[@id="main-container"]//td[1]/a[1]')

        # / html / body / div[3] / div / div[2] / table / tbody / tr[2] / td[1] / div / a / img
        for a in a_list:
            name = a.xpath('./text()').extract_first()
            href = a.xpath('./@href').extract_first()
            url = 'https://www.pianyuan.org' + href
            # url = response.urljoin(href)

            yield scrapy.Request(url=url, callback=self.parse_second, meta={'name': name},dont_filter=True)

    def parse_second(self, response):
        src = response.xpath('//div[@class="container"]//a/img/@src').extract_first()
        name = response.meta['name']
        movie = PianyuanItem(src=src, name=name)
        yield movie

    def start_requests(self):
        headers = {

            'Cookie': self.getCookie(),
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36',
            "Referer": "https://www.pianyuan.org/",
            "Referrer-Policy": "strict-origin-when-cross-origin"
        }

        # 再次请求到详情页，并且声明回调函数callback，dont_filter=True 不进行域名过滤，meta给回调函数传递数据
        yield scrapy.Request(self.start_urls[0], callback=self.parse, dont_filter=True, headers=headers,)
    #
    #
    # # def login_in(self):
    # #     username: w
    # #     password: w
    # #     verify: w
    # #     isremember: 1


# headers = {
#         "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36",
# }
# # 封装好的验证码识别函数
# def tranformImgCode(imgPath,imgType):
#     chaojiying = Chaojiying_Client('用户名', '密码', '软件ID')	        # 用户中心>>软件ID 生成一个替换 软件ID
#     im = open(imgPath, 'rb').read()													#本地图片文件路径 来替换 a.jpg 有时WIN系统须要//
#     return(chaojiying.PostPic(im, imgType))['pic_str']
#
# # 自动获取cookie
# session = requests.Session()
#
# # 识别验证码
# url = 'https://so.gushiwen.cn/user/login.aspx?from=http://so.gushiwen.cn/user/collect.aspx'
# page_text = session.get(url = url,headers = headers).text
# # 解析验证码图片地址
# tree = etree.HTML(page_text)
# img_src = 'https://so.gushiwen.cn/' + tree.xpath('//*[@id="imgCode"]/@src')[0]
# # 将验证码图片保存到本地
# img_data = session.get(img_src,headers = headers).content
# with open('./code.jpg','wb') as fp:
#     fp.write(img_data)
#
# # 识别验证码
# code_text = tranformImgCode('./code.jpg',1902)
# print(code_text)
#
# login_url = 'https://so.gushiwen.cn/user/login.aspx?from=http%3a%2f%2fso.gushiwen.cn%2fuser%2fcollect.aspx'
# data = {
#     '__VIEWSTATE': 'frn5Bnnr5HRYCoJJ9fIlFFjsta310405ClDr+hy0/V9dyMGgBf34A2YjI8iCAaXHZarltdz1LPU8hGWIAUP9y5eLjxKeYaJxouGAa4YcCPC+qLQstMsdpWvKGjg=',
#     '__VIEWSTATEGENERATOR': 'C93BE1AE',
#     'from': 'http://so.gushiwen.cn/user/collect.aspx',
#     'email': '用户名', # 更换自己的用户名
#     'pwd': '密码',     # 更换自己的密码
#     'code': code_text,
#     'denglu': '登录'
# }
# # 对点击登录按钮发起请求,获取登录成功后对应的页面源码数据
# page_text_login = session.post(url = login_url,data = data,headers = headers).text
#
# with open('./gushiwen.html','w',encoding = 'utf-8') as fp:
#     fp.write(page_text_login)
#
#
#
# def imgcode(self, imgPath, imgType):
#     chaojiying = Chaojiying_Client('zihuansama', '123456', '938191')
#     im = open(imgPath, 'rb').read()
#     return (chaojiying.PostPic(im, imgType))['pic_str']
#     session = requests.Session()
#
#     url = 'https://www.pianyuan.org/User/login.html'
#     page_text = session.get(url=url, headers=headers).text
#
#     tree = etree.HTML(page_text)
#     img_src = 'https://pianyuan.org/' + tree.xpath('//div[@class="controls"]/img/@src')[0]
#
#     img_data = session.get(img_src, headers=headers).content
#     with open('./code.jpg', 'wb') as fp:
#         fp.write(img_data)
#
#     code_text = tranformImgCode('./code.jpg', 1902)
#     print(code_text)
#
#     session = requests.Session()
#
#     login_url = 'https://so.gushiwen.cn/user/login.aspx?from=http%3a%2f%2fso.gushiwen.cn%2fuser%2fcollect.aspx'
#     data = {
#
#         'from': 'http://so.gushiwen.cn/user/collect.aspx',
#         'email': '用户名',  # 更换自己的用户名
#         'pwd': '密码',  # 更换自己的密码
#         'code': self.code_text,
#         'denglu': '登录'
#     }
#
#     page_text_login = session.post(url=login_url, data=data, headers=headers).text
#
#     with open('./gushiwen.html', 'w', encoding='utf-8') as fp:
#         fp.write(page_text_login)
