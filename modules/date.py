#!/usr/bin/python
# -*- coding: UTF-8 -*-
import time 
import calendar

#  cpu执行时间 
print time.clock()

#推迟调用线程的运行
time.sleep(3)

# time.time()  返回的是是时间戳，秒数 
localtime = time.localtime(time.time())
print "本地时间为 :", localtime

print time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) 


# 日历 
cal = calendar.month(2016, 1)
print "以下输出2016年1月份的日历:"
print cal

print time.clock()