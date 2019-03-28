# -*- coding:utf8 -*-
import random
import unittest
import sys


class TestSequenceFunctions(unittest.TestCase):
    a = 1

    def setUp(self):
        self.seq = list(range(10))

    @unittest.skip("无条件忽略该方法")
    def test_shuffle(self):
        random.shuffle(self.seq)
        self.seq.sort()
        self.assertEqual(self.seq, list(range(10)))
        print "test_shuffle"

    @unittest.skipIf(a > 5, "condition is not at satified")
    def test_choice(self):
        element = random.choice(self.seq)
        self.assertTrue(element in self.seq)
        print "test_choice"

    @unittest.skipUnless(sys.platform.startswith("linux"),"requires Windows")
    def test_sample(self):
        with self.assertRaises(ValueError):
            random.sample(self.seq, 20)
        print "test_sample"


if __name__ == "__main__":
    testClass = unittest.TestLoader.loadTestsFromTestCase(TestSequenceFunctions)
    suite = unittest.TestSuite(testClass)
    unittest.TextTestRunner(verbosity=2).run(suite)
