#!/usr/bin/python
# -*- coding: UTF-8 -*-

str = 'huahuadavids'
print str[0]
print str[3]
print str[1:4]
print str[1:]
print str * 3
print 'python\nhuahua'
print 'a' in str 

# 格式化输出 类似c语言 
print "My name is %s and weight is %d kg!" % ('Zara', 21)
print '\n\n'

print str.upper()       
print str.capitalize()  
print str.endswith('s')  
print str.find("huad")  #js的indexOf  