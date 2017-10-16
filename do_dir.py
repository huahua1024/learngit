#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from datetime import datetime
import os

'''
pwd = os.path.abspath('.')
print('      Size     Last Modified  Name')
print('------------------------------------------------------------')

for f in os.listdir(pwd):
    fsize = os.path.getsize(f)
    mtime = datetime.fromtimestamp(os.path.getmtime(f)).strftime('%Y-%m-%d %H:%M')
    flag = '/' if os.path.isdir(f) else ''
    print('%10d  %s  %s%s' % (fsize, mtime, f, flag))
'''
'''
# 查看当前目录的绝对路径:
>>> os.path.abspath('.')
'/Users/michael'
# 在某个目录下创建一个新目录，首先把新目录的完整路径表示出来:
>>> os.path.join('/Users/michael', 'testdir')
'/Users/michael/testdir'
# 然后创建一个目录:
>>> os.mkdir('/Users/michael/testdir')
# 删掉一个目录:
>>> os.rmdir('/Users/michael/testdir')
'''
#列出当前目录下的所有目录，只需要一行代码：
#alldir = [x for x in os.listdir('.') if os.path.isdir(x)]
#print(alldir)
#要列出所有的.py文件，也只需一行代码：
#pyfile = [x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py']
#print(pyfile)

#在当前目录以及当前目录的所有子目录下查找文件名包含指定字符串的文件，并打印出相对路径。 
findstr = 'Stu'
pwd = os.path.abspath('.') 

for f in os.listdir('.'):
    if not os.path.isdir(f): #如果当前不是目录而是文件，则查找文件名是否包含指定字符串
        if findstr in f:
            print(os.path.join(pwd, f))
    else:                           #当前是目录，则前往该目录下查找文件
        downpath = os.path.join(pwd, f)  #下一级目录
        for df in os.listdir(downpath):  
            if findstr in df:
                print(os.path.join(downpath, df))

def FindFile(p, s):            #定义函数, 传一个path, 一个str
    print('enter dir==>' + p)
    for x in os.listdir(p):    #遍历path
        if os.path.isdir(os.path.join(p, x)):   #x 是目录。 如果只判断x，会出现误判。要加入整个目录名。
            newP = os.path.join(p, x)   #新path = p + x
            print('####' + newP)
            FindFile(newP, s)           #调用函数自身, 再次遍历这个子目录
        else:                       #X 是文件:
            if s in x:             #查找文件名
                print(os.path.join(p, x))    #打印绝对路径 

    

print('----===========--------')
FindFile(pwd, 'test')

print('----===========--------')
FindFile(pwd, 'do_')
