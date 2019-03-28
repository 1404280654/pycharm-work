from selenium import webdriver
import time
import json
from Ecshop.Browser import OpenBrowser

class GetAllCookie(object):

    def getCSDNcookie(self):
        driver=OpenBrowser("https://passport.csdn.net/account/login")
        driver.find_element_by_xpath("/html/body/div[3]/div/div/div[2]/div/h3/a").click()
        time.sleep(3)
        driver.find_element_by_xpath("//*[@id=\"username\"]").send_keys("13924451750")
        time.sleep(3)
        driver.find_element_by_xpath("//*[@id=\"password\"]").send_keys("kh13530152776")
        time.sleep(3)
        driver.find_element_by_xpath("//*[@id=\"fm1\"]/input[8]").click()
        time.sleep(3)

        dictCookies = driver.get_cookies()#获取登录成功后浏览器cookies
        jsonCookies = json.dumps(dictCookies)#json保存
        # 登录完成后，将cookie保存到本地文件
        with open('Cookie\cookies.json', 'w') as f:
            f.write(jsonCookies)

    def getECSHOPcookie(url):
        driver=OpenBrowser(url)
        driver.find_element_by_xpath("/html/body/form/table/tbody/tr/td[2]/table/tbody/tr[1]/td[2]/input").send_keys("admin")
        time.sleep(3)
        driver.find_element_by_xpath("/html/body/form/table/tbody/tr/td[2]/table/tbody/tr[2]/td[2]/input").send_keys("admin123456")
        time.sleep(3)
        driver.find_element_by_xpath("/html/body/form/table/tbody/tr/td[2]/table/tbody/tr[4]/td[2]/input").click()
        time.sleep(2)

        driver.switch_to_frame("header-frame")
        driver.find_element_by_xpath("// *[ @ id = \"menu-div\"] / ul / li[3] / a").click()
        time.sleep(2)

        #释放定位
        driver.switch_to_default_content()
        #定位frame元素
        print("0")
        m = driver.find_element_by_xpath("//*[@id=\"menu-frame\"]")
        print("1")
        # 再点击下拉框下的选项
        driver.switch_to_frame(m)
        driver.find_element_by_xpath("/html/body/div[2]/div[1]/ul/li[9]/ul/li[6]/a").click()
        time.sleep(10)
        print("2")


        # dictCookies = driver.get_cookies()#获取登录成功后浏览器cookies
        # jsonCookies = json.dumps(dictCookies)#json保存
        # # 登录完成后，将cookie保存到本地文件
        # with open('Cookie\cookiess.json', 'w') as f:
        #     f.write(jsonCookies)

if __name__=="__main__":
    cookie=GetAllCookie()



