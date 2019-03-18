# 1 import 整个模块 
#import hua_print 

#2 按需引入
from hua_print import hprint
hprint("wahaha")

'''
1、当前目录
2、如果不在当前目录，Python 则搜索在 shell 变量 PYTHONPATH 下的每个目录。set PYTHONPATH=/usr/local/lib/python
3、如果都找不到，Python会察看默认路径。UNIX下，默认路径一般为/usr/local/lib/python/

'''