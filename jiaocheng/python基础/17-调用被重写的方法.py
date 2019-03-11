#/usr/bin/env python
#coding=utf8
"""
# Author: kellanfan
# Created Time : Thu 02 Nov 2017 07:54:00 PM CST

# File Name: 16-继承.py
# Description: 继承是子类可以使用父类的方法，可以多层继承

"""

class Animal(object): #父类，基类
    def eat(self):
        print "---吃---"
    def dirik(self):
        print "---喝---"
class Cat(Animal): #括号里写的就是父类，继承父类的方法 子类，派生类
    def catch(self):
        print "---抓老鼠---"
    def jiao(self):
        print "---喵喵叫---"
class Lanmao(Cat):
    def eat(self): #多层继承，重写：继承的方法不太适合子类，可以重写，重新定义
        print "---狂吃---"
    def jiao(self):
        print "---说话了---"
        #第一种调用被重写的方法,不建议用，直接用类名调用父类方法在使用单继承的时候没问题，但是如果使用多继承，会涉及到查找顺序（MRO）、重复调用（钻石继承）等种种问题。
        #Cat.jiao(self) #self要写上
        #第二种,super只能用于新类，就是要加object的
        super(Lanmao, self).jiao()

lan = Lanmao()
lan.jiao()
