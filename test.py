import unittest
from BeautifulReport import BeautifulReport
import main


class TestFunction(unittest.TestCase):
    @classmethod
    def setUp(self):
        print("开始测试")

    @classmethod
    def tearDown(self):
        print("测试结束")

    def text_orig(self):
        print("正在读取orig.txt")
        degree = main.compare(main.readtxt(r'sim_0.8\orig.txt'), main.readtxt(r'sim_0.8\orig.txt'))
        print('相似度为%.2f' % degree)

    def text_add(self):
        print("正在读取orig_0.8_add.txt")
        degree = main.compare(main.readtxt(r'sim_0.8\orig.txt'), main.readtxt(r'sim_0.8\orig_0.8_add.txt'))
        print('相似度为%.2f' % degree)

    def text_del(self):
        print("正在读取orig_0.8_del.txt")
        degree =  main.compare(main.readtxt(r'sim_0.8\orig.txt'), main.readtxt(r'sim_0.8\orig_0.8_del.txt'))
        print('相似度为%.2f' % degree)

    def text_dis_1(self):
        print("正在读取orig_0.8_dis_1.txt")
        degree =  main.compare(main.readtxt(r'sim_0.8\orig.txt'), main.readtxt(r'sim_0.8\orig_0.8_dis_1.txt'))
        print('相似度为%.2f' % degree)

    def text_dis_3(self):
        print("正在读取orig_0.8_dis_3.txt")
        degree =  main.compare(main.readtxt(r'sim_0.8\orig.txt'), main.readtxt(r'sim_0.8\orig_0.8_dis_3.txt'))
        print('相似度为%.2f' % degree)

    def text_dis_7(self):
        print("正在读取orig_0.8_dis_7.txt")
        degree =  main.compare(main.readtxt(r'sim_0.8\orig.txt'), main.readtxt(r'sim_0.8\orig_0.8_dis_7.txt'))
        print('相似度为%.2f' % degree)

    def text_dis_10(self):
        print("正在读取orig_0.8_dis_10.txt")
        degree =  main.compare(main.readtxt(r'sim_0.8\orig.txt'), main.readtxt(r'sim_0.8\orig_0.8_dis_10.txt'))
        print('相似度为%.2f' % degree)

    def text_dis_15(self):
        print("正在读取orig_0.8_dis_15.txt")
        degree =  main.compare(main.readtxt(r'sim_0.8\orig.txt'), main.readtxt(r'sim_0.8\orig_0.8_dis_15.txt'))
        print('相似度为%.2f' % degree)

    def text_mix(self):
        print("正在读取orig_0.8_mix.txt")
        degree =  main.compare(main.readtxt(r'sim_0.8\orig.txt'), main.readtxt(r'sim_0.8\orig_0.8_mix.txt'))
        print('相似度为%.2f' % degree)

    def text_rep(self):
        print("正在读取orig_0.8_rep.txt")
        degree =  main.compare(main.readtxt(r'sim_0.8\orig.txt'), main.readtxt(r'sim_0.8\orig_0.8_rep.txt'))
        print('相似度为%.2f' % degree)


if __name__ == '__main__':
    suite = unittest.TestSuite()
    tests = [
        TestFunction('text_orig'),
        TestFunction('text_add'),
        TestFunction('text_del'),
        TestFunction('text_dis_1'),
        TestFunction('text_dis_3'),
        TestFunction('text_dis_7'),
        TestFunction('text_dis_10'),
        TestFunction('text_dis_15'),
        TestFunction('text_mix'),
        TestFunction('text_rep')
    ]
    suite.addTests(tests)
    BeautifulReport(suite).report(filename='TestReport.html',
                                  description='论文查重报告',
                                  log_path='.')
