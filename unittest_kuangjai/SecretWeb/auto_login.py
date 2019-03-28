from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from commom_module.Excel import read_excel


dr = webdriver.Firefox()
base_url = 'file:///C:/Users/Testing/AppData/Roaming/Skype/My%20Skype%20Received%20Files/secretFormal/index.html#/tradingCenter/login'
dr.get(base_url)
user_list=[]
pass_list=[]

def setUpClass():
    list=read_excel()
    user_list.append(list[0])
    pass_list.append(list[1])
    print(user_list)

def tearDownClass():
    sleep(5)
    dr.quit()

def test_login(number):
    if(number!=0):
        js = 'window.open("file:///C:/Users/Testing/AppData/Roaming/Skype/My%20Skype%20Received%20Files/secretFormal/index.html#/tradingCenter/login");'
        dr.execute_script(js)
        # handles = dr.window_handles
        # print(handles)
        # dr.switch_to_window(handles[number+1])
        print("————————————————")
        print(dr.current_window_handle)  # 输出当前窗口句柄（百度）
        handles = dr.window_handles  # 获取当前窗口句柄集合（列表类型）
        print(handles)  # 输出句柄集合
        print(number)
        for handle in handles:  # 切换窗口（切换到搜狗）
            dr.switch_to_window(handles[int(number)])
            print(dr.current_window_handle)  # 输出当前窗口句柄（搜狗）
            break
        handles = []

    zhahao=WebDriverWait(dr,3).until(
         EC.presence_of_element_located((By.XPATH, "//*[@id=\"app\"]/div[2]/div[1]/div/input[1]"))
     )
    zhahao.send_keys(str(user_list[0][number]))
    sleep(1)
    dr.find_element_by_xpath("//*[@id=\"app\"]/div[2]/div[1]/div/input[2]").send_keys(str(pass_list[0][number]))
    sleep(1)
    dr.find_element_by_xpath("//*[@id=\"app\"]/div[2]/div[1]/div/button").click()
    sleep(1)

    try:
        dr.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/button").click()
        sleep(2)
        print("账号密码错误")
        #dr.close()
    except(Exception):
        print("密码对了")


if __name__ == '__main__':
     setUpClass()
     for i in range(1,5):
         test_login(i-1)
     tearDownClass()