#!/usr/bin/python
# -*- coding: UTF-8 -*-

obj1 = {'name': 'haha'}
obj2 = {}

# {} == {} true 
print obj1 == obj2 

num1 = 1
num2 = 4
flag1 = num1 > 0
flag2 = num2 > 0
if flag1 and flag2:
  print "都大于0"

### in 在不在
list1_num = 1
list1 = [1,2222,33333,5]

print list1_num in list1 