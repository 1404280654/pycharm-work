# coding:utf-8
from HTMLTestRunner import HTMLTestRunner
import unittest,time,os
import test
import sys
#获取当个文件路径
test_case_ = os.path.dirname(os.path.realpath(__file__))
print(test_case_)
print("---------------------")
#个test_case_添加多一层testcase路径
test_case = os.path.join(test_case_,'SecretWeb')
print(test_case)
print("---------------------")
#个test_case_添加多一层report路径
test_report = os.path.join(test_case_,'report')
print(test_report)
print("---------------------")

#unittest.defaultTestLoader(): defaultTestLoader()类，通过该类下面的discover()方法可自动更具测试目录start_dir
# 匹配查找测试用例文件（test*.py），并将查找到的测试用例组装到测试套件，因此可以直接通过run()方法执行discover。
test_list = unittest.defaultTestLoader.discover(test_case ,pattern='test*.py')



if __name__ == '__main__':
    now = time.strftime('%Y_%m_%d_%H_%M_%S')
    print(now)
    filename = test_report+'\\'+now+'_result.html'
    print(filename)
    fp = open(filename, 'wb')
    runner = HTMLTestRunner(stream=fp,
                          title=u"百度——有道测试项目",
                          description='Window10 Chrome browser 62.0 version')
    #运run()方法是运行测试套件的测试用例，入参为test_list测试套件。
    runner.run(test_list)
    fp.close()


