# coding:utf-8
"""
Name : demo1.py
Author  : Mark
Contect : hongming666@outlook.com
Time    : 2022/6/25 18:08
Desc:
"""
import hashlib
import time
from random import randint, sample

import requests


def hex5(value):
    """
    将value进行md5加密处理
    :param value: action+time+randstr
    :return: hex5 value
    """
    manipulator = hashlib.md5()
    manipulator.update(value.encode('utf-8'))
    sign = manipulator.hexdigest()
    return sign


def main():
    """
    主函数
    """
    # 生成1-9之间的随机5个数
    action = "".join([str(randint(1, 9)) for _ in range(5)])
    # 生成当前时间戳
    tim = round(time.time())
    # 生成5个随机大写字母
    randstr = "".join(sample([chr(_) for _ in range(65, 91)], 5))
    sign = action + str(tim) + randstr

    args = uri(action, tim, randstr, hex5(sign))
    headers = {
        'Referer': 'http://www.porters.vip/verify/sign/',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest'
    }

    url = "http://www.porters.vip/verify/sign/fet" + args
    response = requests.get(url=url, headers=headers)
    print(response.text)

def uri(action, tim, randstr, sign):
    args = '?actions={}&tim={}&randstr={}&sign={}'.format(action, tim, randstr, sign)
    return args


if __name__ == '__main__':
    main()
