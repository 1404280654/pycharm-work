# -*- coding:utf8 -*-
import unittest


class myclass(object):
    @classmethod
    def sum(cls,a,b):
        return a+b

    @classmethod
    def sub(cls,a,b):
        return a-b

class mytest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """初始化类固件，整个测试流程开始前执行一次"""
        print "- - - setUpClass"

    @classmethod
    def tearDownClass(cls):
        """重构类固件，整个测试流程结束后执行一次"""
        print "- - - setDownClass"

    # 初始化工作
    def setUp(self):
        """每个测试case前执行一次"""
        self.a=3
        self.b=1
        print "- - setUp"

    # 退出清理工作
    def tearDown(self):
        """每个测试case结束执行一次"""
        print "- - tearDown"

    # 具体测试用例
    def testsum(self):
        self.assertEqual(myclass.sum(self.a,self.b), 4 ,'test summ fail')

    def testsub(self):
        self.assertEqual(myclass.sub(self.a, self.b), 2, 'test summ fail')


if __name__ == '__main__':
    unittest.main()
    
""" 执行结束后，每个点的意思表示，一个测试case成功通过
    而出现E则表示有一个测试用例本身有异常
    而出现F则表示有一个测试用例执行失败
"""