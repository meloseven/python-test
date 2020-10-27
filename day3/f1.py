#!/usr/bin/python3
from datetime import date
import os
print(__file__)
print(os.getcwd())
print(os.path.join(os.path.dirname(__file__), 'file/f1.txt'))

f = open('day3/file/f1.txt', 'w+')

today=date.today()
f.write(f'哈哈哈，我是meloseven\n{today}')

f.close()