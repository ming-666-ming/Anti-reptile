# coding:utf-8
"""
Name : demo1.py
Author  : Mark
Contect : hongming666@outlook.com
Time    : 2022/6/25 17:02
Desc:   crawl steamboat news
"""

import requests
from pyquery import PyQuery as pq

def main():
    """
    主函数
    """
    url = "http://www.porters.vip/verify/cookie/content.html"
    headers = {
        'Cookie': 'isfirst=789kq7uc1pp4c'
    }
    try:
        response = requests.get(url=url, headers=headers)
        if response.status_code == 200:
            html = pq(response.text)
            content = html.css('col-md-10').find('p').text()
            print(content)
            # for content_p in content:
            #     content_p = content_p.find('p').text()
            #     print(content_p, end='\n')
    except requests.ConnectionError as e:
        print(e)

if __name__ == '__main__':
    main()