import time

from selenium import webdriver
from chaojiying import Chaojiying_Client
from selenium.webdriver.common.by import By
import requests


driver=webdriver.Chrome()
base_url='https://www.pianyuan.org/User/login.html'
index_url='https://www.pianyuan.org/?p=1'
driver.get(base_url)
img=driver.find_element(By.XPATH,'/html/body/div[2]/div/section/div/form/div[4]/div/img').screenshot_as_png
chaojiying=Chaojiying_Client('zihuansama', '123456', '938191')
dic = chaojiying.PostPic(img, 1005)
verifyimg=dic['pic_str']
USERNAME='694258692@qq.com'
PASSWORD='w526079.'
driver.find_element(By.XPATH,'/html/body/div[2]/div/section/div/form/div[1]/div/input').send_keys(USERNAME)
driver.find_element(By.XPATH,'/html/body/div[2]/div/section/div/form/div[2]/div/input').send_keys(PASSWORD)
driver.find_element(By.XPATH,'/html/body/div[2]/div/section/div/form/div[3]/div/input').send_keys(verifyimg)
time.sleep(3)
driver.find_element(By.XPATH,'/html/body/div[2]/div/section/div/form/div[6]/div/button').click()
time.sleep(3)

cookies = driver.get_cookies()
print('Cookies', cookies)
driver.close()

# set cookies to requests
session = requests.Session()
for cookie in cookies:
    session.cookies.set(cookie['name'], cookie['value'])


response_index = session.get(index_url)
# print('Response Status', response_index.status_code)
# print('Response URL', response_index.content)
