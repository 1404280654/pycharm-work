from selenium import webdriver
import time
import json

def logincookie(url):
    driver=webdriver.Chrome()
    #driver.get("https://www.csdn.net/")
    driver.get(url)
    # 删除第一次建立连接时的cookie
    driver.delete_all_cookies()
    # 读取登录时存储到本地的cookie
    with open('Cookie\cookies2.json', 'r', encoding='utf-8') as f:
        listCookies = json.loads(f.read())

    #拆分URL获取cookie的doaim
    fen=url.split(".")
    asd="."+fen[1]+"."+fen[2]
    doaim=asd[:-1]

    for cookie in listCookies:
        driver.add_cookie({
            'domain': doaim,  # 此处xxx.com前，需要带点
            'name': cookie['name'],
            'value': cookie['value'],
            'path': '/',
            'expires': None
        })
    driver.get(url)#打开url，实现免登陆

if __name__=="__main__":
    logincookie()


