#!/usr/bin/env python
# *_*coding:utf-8 *_*
"""
    @Author:    Howard Zhu
    @Date:      2019-5-9
    @File:      classFib.py
    @Software:  PyCharm 
"""


class Fib(object):
    def __init__(self):
        self.a = 0
        self.b = 1

    def __iter__(self):
        return self

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        if self.a > 10000:
            raise StopIteration()
        return self.a

