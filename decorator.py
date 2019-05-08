#!/usr/bin/env python
# *_*coding:utf-8 *_*
"""
    @Author:    Howard Zhu
    @Date:      2019-5-7
    @File:      decorator.py
    @Software:  PyCharm 
"""
import functools, time


def log(*, text='calling'):
    def metric(fn):
        @functools.wraps(fn)
        def wrapper(*args, **kwargs):
            print('Begin %s %s()...' % (text, fn.__name__))
            start_time = time.time()
            exec_func = fn(*args, **kwargs)
            end_time = time.time()
            exec_time = end_time - start_time
            print('End %s %s()!' % (text, fn.__name__))
            print('Time: %.2fs' % exec_time)
            return exec_func
        return wrapper
    return metric


@log()
def f():
    print("Hello, world!")


if __name__ == '__main__':
    f()
