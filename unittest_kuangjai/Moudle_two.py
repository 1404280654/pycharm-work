# -*- coding:utf8 -*-
import random
import unittest


class TestSequenceFunction(unittest.TestCase):

    def setUp(self):
        self.seq=range(10)

    def tearDown(self):
        pass

    def test_choice(self):
        element = random.choice(self.seq)
        self.assertTrue(element in self.seq)
        print "test_choice"

    def test_sample(self):
        with self.assertRaises(ValueError):
            random.sample(self.seq, 20)
        for element in random.sample(self.seq, 5):
            self.assertTrue(element in self.seq)
        print 'test_sample'



# class TestDictValueFormatFunction(unittest.TestCase):
#     def setUp(self):
#         self.seq = range(10)
#
#     def tearDown(self):
#         pass
#
#     def test_shuffle(self):
#         random.shuffle(self.seq)  # 打乱顺序
#         self.seq.sort()
#         self.assertEqual(self.seq, range(10))
#         self.assertRaises(TypeError, random.shuffle, (1, 2, 3))
#         print 'test_shuffle'

# if __name__=='__main__':
#     """根据给定的测试类，获取其中的所有以test开头的测试方法，并且返回一个测试套件"""
#     testCase1 = unittest.TestLoader().loadTestsFromTestCase(TestSequenceFunction)
#     testCase2 = unittest.TestLoader().loadTestsFromTestCase(TestDictValueFormatFunction)-+
#     """将多个测试类加载到测试套件中"""
#     suite = unittest.TestSuite([testCase1, testCase2])
#     unittest.TextTestRunner(verbosity=0).run(suite)

    """如果要用力按顺序执行  使用这种方法"""


if __name__ == '__main__':
    suite = unittest.TestSuite()
    # suite.addTest(TestDictValueFormatFunction("test_shuffle"))
    suite.addTest(TestSequenceFunction("test_sample"))
    suite.addTest(TestSequenceFunction("test_choice"))

    runner = unittest.TextTestRunner()
    runner.run(suite)