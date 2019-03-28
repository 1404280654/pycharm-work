import unittest
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from commom_module.Excel import read_excel


class MyTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        list=read_excel()
        user_list=list[0]
        pass_list=list[1]
        print(user_list)
        print(pass_list)
        cls.dr = webdriver.Firefox()
        cls.base_url = 'file:///C:/Users/Testing/AppData/Roaming/Skype/My%20Skype%20Received%20Files/secretFormal/index.html#/tradingCenter/login'

    @classmethod
    def tearDownClass(cls):
        sleep(5)
        cls.dr.quit()

    def test_login(self,number):
        self.dr.get(self.base_url)
        try:
            zhahao=WebDriverWait(self.dr,3).until(
                 EC.presence_of_element_located((By.XPATH, "//*[@id=\"app\"]/div[2]/div[1]/div/input[1]"))
             )
        finally:
            print("失败")
        zhahao.send_keys("souhu156273")
        sleep(1)
        self.dr.find_element_by_xpath("//*[@id=\"app\"]/div[2]/div[1]/div/input[2]").send_keys("Aa123456")
        sleep(1)
        self.dr.find_element_by_xpath("//*[@id=\"app\"]/div[2]/div[1]/div/button").click()



if __name__ == '__main__':
    unittest.main()
    # 定义一个单元测试容器
    # suiteTest = unittest.TestSuite()
    # # # 将测试用例加入到容器
    # for i in range(1,5):
    #     a=get_list(i)
    #     print(a)
    #     suiteTest.addTest(MyTestCase("test_login"))