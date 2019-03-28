from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Firefox()
driver.get("file:///D:/demo.html")

#下拉列表
a=driver.find_element_by_xpath("//*[@id=\"select\"]/select").click()
driver.find_element_by_xpath("//*[@id=\"select\"]/select/option[2]").click()

#单选按钮
driver.find_element_by_xpath("//*[@id=\"radio\"]/input[3]").click()

#多选按钮
inputs = driver.find_elements_by_tag_name('input')
#然后从中过滤出 tpye 为 checkbox的元素，单击勾选
print(inputs)
for input in inputs:
     if input.get_attribute('type') == 'checkbox':
         input.click()
time.sleep(1)

#点击Alert
driver.find_element_by_xpath("//*[@id=\"alert\"]/input").click()
alert = driver.switch_to_alert().text #或则.accept,default
time.sleep(1)
driver.switch_to_alert().accept()
time.sleep(2)
#接收警告信息：确定
print(alert)


#点击文件选择
driver.find_element_by_xpath("//*[@id=\"load\"]").send_keys("F:\\asdf.csv")


#打开新窗口
# nowhandle=driver.current_window_handle
# print (driver.current_window_handle)
# time.sleep(3)
# driver.find_element_by_css_selector("a[class='open']").click()
# handles = driver.window_handles
# driver.switch_to.window(handles[1])
# print (driver.current_window_handle)
# #以下为补充#############################################################################

#获得所有窗口
# allhandles=driver.window_handles
# #循环判断窗口是否为当前窗口
# for handle in allhandles:
#     if handle != nowhandle:
#         driver.switch_to_window(handle)
#         print ('now register window!')
#回到原先的窗口

# driver.close()
# driver.switch_to_window(nowhandle)
#





# #移动到地方，有东西显示
# q=driver.find_element_by_xpath("//*[@id=\"action\"]/input")
# action = ActionChains(driver)
# action.move_to_element(q).perform()
#
# #循环点击
# b=driver.find_element_by_css_selector("input[class='wait']")
# b.click()
# b.click()
# b.click()



#保留疑问
# input=driver.find_elements_by_xpath("//input[@type='checkbox']")
# for inpt in input:
#     if input.get_attribute('type') == 'checkbox':
#         input.click()
