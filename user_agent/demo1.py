# coding:utf-8
"""
Name : demo1.py
Author  : Mark
Contect : hongming666@outlook.com
Time    : 2022/6/22 18:16
Desc:   User agent anti crawler bypass practice。
"""

import requests
from parsel import Selector

try:
    url = "http://www.porters.vip/verify/uas/index.html"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9"
    }
    resp = requests.get(url=url, headers=headers)
    if resp.status_code == 200:
        sel = Selector(resp.text)
        res = sel.css('.media-heading a::text').extract()
        print(res)
except requests.ConnectionError as e:
    print("连接错误")