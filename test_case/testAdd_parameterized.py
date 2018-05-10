#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/12 22:59
# @Author  : wengy
# @Email   : 1915992513@qq.com
# @Blog    : http://www.cnblogs.com/UncleYong/
# @GitHub  : https://github.com/UncleYong


import os,sys
path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, path)
import unittest
from core import HTMLTestRunner
from parameterized import parameterized
from core import logger
import inspect
from core.tools import p

def cacl(a, b):
    return a+b


class MyCacl2(unittest.TestCase):
    def setUp(self):
        pass
        # print('测试用例开始执行...')

    def tearDown(self):
        pass
        # print('测试用例执行完成...')

    @parameterized.expand(
        [
            (1, 2, 3, '整数相加'),  # 整数相加
            (1.5, 2, 3.5, '小数加整数'),  # 小数加整数
            (1.5, 2.6, 4.1, '小数相加'),  # 小数相加
            (-1, 2, 1, '负数加整数'),  # 负数加整数
            (-1,1.5,0.5, '负数加小数'),  # 负数加小数
            (-1,-2,-3, '负数相加'),  # 负数相加
            (0,1,1, '0加整数'),  # 0加整数
            (0,0.5,0.5, '0加小数'),  # 0加小数
            (0,-1,-1, '0加负数'),  # 0加负数
            (1,"",1, '整数加空'),  # 整数加空
            (1,"a",1, '整数加字母'),  # 整数加字母
            (1,"$",1, '整数加特殊字符')  # 整数加特殊字符
        ]
    )
    
    def test_cacl(self, a, b, c, d):
        try:
            res = cacl(a, b)
        except TypeError as e:
            res = '类型错误'
        logger.logger.logger.debug('是测试点"%s"下的用例"%s",返回的结果res=%s]'%(self.__class__.__name__, d, res))

        self.assertEqual(res, c)
    #     
    #     
    @staticmethod
    def get_current_function_name():
        return inspect.stack()[1][3]

    # def test_int_int(self):
    #     """整数加整数"""
    #     res = cacl(1, 1)
    #     logger.logger.logger.debug('当前方法: %s'%p.get_current_function_name())
    #     logger.logger.logger.debug('是测试点"%s"下的用例"%s",返回的结果res=%s]'%(self.__class__.__name__, getattr(self, p.get_current_function_name()).__doc__, res))
    #     self.assertEqual(res, 2)

    # def test_int_float(self):
    #     """整数加小数"""
    #     res = cacl(1, 2.8)
    #     logger.logger.logger.debug('是测试点"%s"下的用例"%s",返回的结果res=%s]'%(self.__class__.__name__, getattr(self, p.get_current_function_name()).__doc__, res))
    #     self.assertEqual(res, 3.8)

    # def test_int_negativeNumber(self):
    #     """整数加负数"""
    #     res = cacl(1, -5)
    #     logger.logger.logger.debug('是测试点"%s"下的用例"%s",返回的结果res=%s]'%(self.__class__.__name__, getattr(self, p.get_current_function_name()).__doc__, res))
    #     self.assertEqual(res, -4)

    # def test_int_letter(self):
    #     """整数加字母"""
    #     try:
    #         res = cacl(1, 'a')
    #     except TypeError as e:
    #         res = '类型错误'
    #     logger.logger.logger.debug('是测试点"%s"下的用例"%s",返回的结果res=%s]'%(self.__class__.__name__, getattr(self, p.get_current_function_name()).__doc__, res))
    #     self.assertEqual(res, -4)

# if __name__ == '__main__':
#     suit = unittest.TestSuite()
#     suit.addTest(MyCacl("test_int_int"))
#     suit.addTest(MyCacl("test_int_float"))
#     suit.addTest(MyCacl("test_int_negativeNumber"))
#     suit.addTest(MyCacl("test_int_letter"))
#     fp = open("./report.html","wb")
#     runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u'**项目测试报告',description=u'测试结果')
#     runner.run(suit)
#     fp.close()
#
if __name__ == '__main__':
    unittest.main()