from redis import StrictRedis
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from multiprocessing import Process, Queue
from bs4 import BeautifulSoup
import random
import re
import time

tel = "your telephone number"
pas = "your password"
base_url = "https://maimai.cn/contact/detail/"

redis = StrictRedis(host='your host', port=6379, db=8, password='WonderALY1')
#8 号数据库
chromeOptions = webdriver.ChromeOptions()
browser = webdriver.Chrome(chrome_options=chromeOptions)
browser.get("https://acc.maimai.cn/login")

wait = WebDriverWait(browser, 10)
input = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'loginPhoneInput')))
input.send_keys(tel)

password = wait.until(EC.presence_of_element_located((By.ID, 'login_pw')))
password.send_keys(pas)
btn = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'loginBtn')))
btn.click()


#ai = ['计算机视觉', '人工智能', '自然语言处理', '机器学习', '深度学习']


def get_profile(browser):
    links = list()
    for n in range(100):
        browser.get("https://maimai.cn/search/contacts?count=20&page="+str(n)+"&query=人工智能&dist=0&searchTokens=&highlight=true&jsononly=1&pc=1")
        json_text = browser.page_source
        g = re.findall('"encode_mmid":"(.*?)"', json_text)

        for i in g:
            links.append(i)
            print(redis.sadd('mt', i))
        time.sleep(8)
    return links


def get_companies(browser):
    id = redis.sunion(['mt'])
    red = StrictRedis(host='47.94.246.65', port=6379, db=12, password='WonderALY1')
    for s in id:
        tt = random.randint(10, 18)
        time.sleep(tt)
        try:
            browser.get("https://maimai.cn/contact/detail/" + s.decode('utf-8'))
            wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'title')))
            response = browser.page_source
            r = BeautifulSoup(response, 'lxml')

            pos = r.find_all(class_='experience-card')
            l = list()
            for i in pos:
                company = i.find(class_="title")
                l.append(company.text.split('•')[0].strip())
            #print(l)
            c = len(l) + 0.0
            print(l)
            for j in l:
                   
                print(red.zincrby('count_mt', c, j))
                c -= 1.0
        except:
            pass
                # l.append(year.text)



id = get_profile(browser)
#get_companies(browser)
res = redis.sunion(['mt'])
print(len(res))

