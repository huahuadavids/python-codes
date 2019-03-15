#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
- 类型属于对象，变量是没有类型的
- 整数、字符串、元组是不可变数据 
- python 的 None 类似于 js中的undefined 
'''

'''
默认参数 关键词参数(调用加参数名字)

'''
# def myPrint(str = 'default-haha'):
#     print '--------'
#     print str

# myPrint('haha')
# myPrint( str = 'wahahaha')
# myPrint()

# ints  = 1 
# ints  = 2
# print type(ints)
# ints  = [1]
# print type(ints)


'''
多余参数 strs 是一个元组 
'''
def demo(str, *strs):
    print str, strs 
    print type(strs) 

demo(1,2,3,4)    

'''
lambda 匿名函数
'''

add = lambda x, y : x +y ;

print add(1,2)
