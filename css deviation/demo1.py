# coding:utf-8
"""
Name : demo1.py
Author  : Mark
Contect : hongming666@outlook.com
Time    : 2022/6/27 11:15
Desc:   css deviation
"""
import re

from parsel import Selector
import requests


def main():
    """
    主函数
    """
    url = "http://www.porters.vip/confusion/flight.html"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36',
    }
    response = requests.get(url=url, headers = headers)
    sel = Selector(response.text)

    em = sel.css('em.rel').extract()
    for element in em:
        element = Selector(element)
        # 提取b标签的style属性值
        element_b = element.css('b').extract()
        alternate_price = []
        # 获取第一队<b>标签中列表的值
        b1 = Selector(element_b.pop(0))
        base_price = b1.css('i::text').extract()
        for eb in element_b:
            ebs = Selector(eb)
            style = ebs.css('b::attr("style")').get()
            # 获取具体位置
            position = ''.join(re.findall('left:(.*?)px', style))
            # 获取该标签下的数字
            value = ebs.css('b::text').get()
            alternate_price.append({'position':position, 'value':value})
        for al in alternate_price:
            position = int(al.get('position'))
            value = al.get('value')
            index = int(position / 16)
            base_price[index] = value
        print(base_price)


if __name__ == '__main__':
    main()