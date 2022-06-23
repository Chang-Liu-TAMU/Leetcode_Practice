# @Time: 2022/5/12 20:06
# @Author: chang liu
# @Email: chang_liu_tamu@gmail.com
# @File:test.py
import re
def gen():
    a = 90
    if a == 10:
        yield 100

g = gen()
print(type(g))
print(list(g))