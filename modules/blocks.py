#!/usr/bin/python
# -*- coding: UTF-8 -*-
print "Hello, World 花花!"
'''
# statement 
num = 0 
if num > 1:
  print("num > 1")
else:
  print("num < 1") 


# python 没有 switch 语句 
# for 
for letter in 'banana' :
  print "letter + " + letter 

# while 
count = 0
while count < 5 :
  print "count = " , count
  count+=1 
else :
  print "count >= 5"  
'''
# 遍历list

list1 = ['demo1', 'demo2']

for item in list1:
  print item


for index in range(len(list1)):
  print list1[index]

# break 
for letter in 'Python':     # 第一个实例
   if letter == 'h':
      break
   print '当前字母 :', letter

#continue 
for letter in 'Python':     # 第一个实例
   if letter == 'h':
      continue
   print '当前字母 :', letter