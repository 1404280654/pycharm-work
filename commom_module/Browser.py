# coding='utf-8'
from selenium import webdriver
from time import sleep

def OpenBrowser(url):
    driver = webdriver.Chrome()  # 选择打开的浏览器
    driver.maximize_window()  # 浏览器窗口最大化
    driver.implicitly_wait(2)  # 隐式等待
    driver.get("https://www.baidu.com/")  # 获取URL，打开页面
    sleep(1)  # 直接等待
    return driver

if __name__=='__main__':
    OpenBrowser("https://www.baidu.com/")

#
# path = "D:/ordinary-software/Chrome/Application"# 注意这个路径需要时可执行路径（chmod 777 dir or 755 dir）
# def chrome_options():
#     mobile_emulation = {"deviceMetrics": {"width":375, "height": 667, "pixelRatio": 2.0},        "userAgent":"Mozilla/5.0 (Linux; U; Android 4.0.4; en-gb; GT-I9300 Build/IMM76D) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30"        }
#     chrome_options = webdriver.ChromeOptions()
#     chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
#     return chrome_options
#
# driver = webdriver.Chrome(executable_path=path, chrome_options=chrome_options())
