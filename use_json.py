#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pickle

d = dict(name='bob', age=20, score=88)
print(d)
da = pickle.dumps(d)
print(da)

reborn = pickle.loads(da)
print(reborn)

########################
import json
d = dict(name='Sun', age=40, score=58)
print(d)
da = json.dumps(d)
print('JSON Data is a str:{}'.format(da))
reborn = json.loads(da)
print(reborn)

class Stu(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score
    
    def __str__(self):
        return 'Stu object(%s, %s, %s)'%(self.name, self.age, self.score)

s = Stu('Hua', 35, 99)
std_data = json.dumps(s, default=lambda obj:obj.__dict__)
print('Dump Stu:', std_data)
rebuild = json.loads(std_data, object_hook=lambda d:Stu(d['name'],d['age'],d['score']))
print(rebuild)
re = json.loads(std_data)
print(re)