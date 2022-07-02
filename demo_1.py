# coding:utf-8
"""
Name : demo_1.py
Author  : Mark
Contect : hongming666@outlook.com
Time    : 2022/6/30 9:05
Desc:
"""
import re
astr = '''aaaaa何时when 杖尔看see南雪snow，我me与梅花plum blossom两白头'''
res = ''.join(re.findall('[\u4e00-\u9fa5]', astr))
print(res)
