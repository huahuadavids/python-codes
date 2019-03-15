#!/usr/bin/python
# -*- coding: UTF-8 -*-

dict1 = {
    'name' : 'david',
    'sex' : 'male',
}
dict1['age'] = 1111;

print dict1
del dict1['age'] 
print dict1

print type(dict1)
print len(dict1)
print str(dict1)


dict1.clear()
print dict1;

list1 = [1,3,4]
dict2 = dict.fromkeys(list1)
print dict2 
dict3 = dict.copy(dict2)
print dict3 


## 字典 js的 obj
obj = {}
obj['name'] = 'lala'
obj['age'] = 11 
print obj.keys()
print obj.values()
'''