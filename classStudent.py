#!/usr/bin/env python
# *_*coding:utf-8 *_*
"""
    @Author:    Howard Zhu
    @Date:      2019-5-7
    @File:      classStudent.py
    @Software:  PyCharm 
"""


class Studentd:
    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def print_score(self):
        print("%s \'s score is %s" %(self.__name, self.__score))

    def get_name(self):
        return self.__name

    def set_score(self, score):
        if 0 <= score <= 100:
            self.__score = score
        else:
            print('Please enter the valid value!')


class Student(object):
    def __init__(self, name, gender):
        self.name = name
        self.__gender = gender

    def get_gender(self):
        return self.__gender

    def set_gender(self, gender):
        if gender != 'male' and gender != 'female':
            print('Please enter the valid gender!')
        else:
            self.__gender = gender

    def __str__(self):
        return 'Student object:(name: %s, gender: %s)' % (self.name, self.__gender)

    __repr__ = __str__


bart = Student('Bart', 98)
lisa = Student(name='Lisa', gender=60)

a = []