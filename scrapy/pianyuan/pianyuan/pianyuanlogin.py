from selenium import webdriver
import time
import requests

from selenium.webdriver.common.by import By



base_url='https://pianyuan.org/User/login.html'
# login_url='https://pianyuan.org/User/login.html'
# index_url='https://pianyuan.org/?p=1'
# username='694258692@qq.com'
# password='w526079.'


driver=webdriver.Chrome()

# # username: 694258692@qq.com
# # password: w526079.
# # verify:
# # isremember: 1
#inputEmail

# driver.get(base_url)
# time.sleep(6)
# driver.add_cookie({"name": "PHPSESSID", "value": "bb5ednuiolv4lo6f3i8h9tpre3"})
# driver.add_cookie({"name": "security_session_verify", "value": "434b1776d9aa3516f7a280ab65a3642e"})
# driver.add_cookie({"name": "PHPSESSID", "value": "bb5ednuiolv4lo6f3i8h9tpre3"})
# driver.add_cookie({"name": "security_session_verify", "value": "434b1776d9aa3516f7a280ab65a3642e"})
#
# time.sleep(6)
# driver.get("https://www.pianyuan.org/mv")
#
#
# time.sleep(6)

# cks = driver.get_cookies()
# for ck in cks:
#     print(ck)
# time.sleep(50)
# for ck in cks:
#     print(ck)

#
# 'domain': 'pianyuan.org', 'httpOnly': False, 'name': 'PHPSESSID', 'path': '/', 'secure': False, 'value': 'bb5ednuiolv4lo6f3i8h9tpre3'}
# {'domain': 'pianyuan.org', 'expiry': 1662070676, 'httpOnly': True, 'name': 'security_session_verify', 'path': '/', 'secure': False, 'value': '434b1776d9aa3516f7a280ab65a3642e'}
# {'domain': 'pianyuan.org', 'httpOnly': False, 'name': 'PHPSESSID', 'path': '/', 'secure': False, 'value': 'bb5ednuiolv4lo6f3i8h9tpre3'}
# {'domain': 'pianyuan.org', 'expiry': 1662070676, 'httpOnly': True, 'name': 'security_session_verify', 'path': '/', 'secure': False, 'value': '434b1776d9aa3516f7a280ab65a3642e'}

PHPSESSID = d5ivgr3dqjbimglaq65eqmpql0;
security_session_verify = 3
d9b3d32515920f60ac5bf5d4bea0ea6;
py_loginauth = WyI2OTQyNTg2OTJAcXEuY29tIiwxNjYxNzkzMTc3LCJmZTg5ZjU3MTkzYzJjODM0Il0 % 3
D
# driver.find_element(By.css.selector,'#inputEmail').send_keys(username)
# driver.find_element(By.css.selectors'#inputPassword').send_keys(password)
# driver.find_element(By.css.selector,'#main-container > div > section > div > form > div:nth-child(6) > div > button').click()
# time.sleep(10)
# current_handle = driver.current_window_handle
#
# handles = driver.window_handles
#m
# for handle in handles:
#
#            driver.switch_to.window(handle)
#
#            time.sleep(1)
#
#            print(driver.title, driver.current_window_handle)
#
#            driver.close()
#
#            time.sleep(1)
#
# cookies = driver.get_cookies()
# print('Cookies', cookies)
# session = requests.Session()
# for cookie in cookies:
#     session.cookies.set(cookie['name'], cookie['value'])
#
# response_index = session.get(index_url)

# //*[@id="main-container"]/div/section/div/form/div[4]/div/img
# headers={
#
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
#     'Referer':' https://pianyuan.org/User/login.html'
# }
#
#
# date={
#
#         'username': '694258692 @ qq.com',
#         'password': 'w526079.',
#         'verify':'',
#         'isremember': '1'
#  }
# response=requests.post(base_url,date=date,headers=headers)
