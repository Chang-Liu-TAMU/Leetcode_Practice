# @Time: 2022/5/12 20:06
# @Author: chang liu
# @Email: chang_liu_tamu@gmail.com
# @File:test.py

class obj:
    def __getitem__(self, item):
        return item

o = obj()
print(o[1])