# coding:utf-8
"""
Name : demo1.py
Author  : Mark
Contect : hongming666@outlook.com
Time    : 2022/6/27 10:25
Desc:   Identify mobile phone number
"""
import io
import requests
import pytesseract
from PIL import Image
def main():
    """
    主函数
    """

    url = "http://www.porters.vip/confusion/phonenumber.png"
    headers = {
        'Referer': 'http://www.porters.vip/confusion/recruit.html',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.3'
    }
    response = requests.get(url=url, headers=headers).content
    image_stream = Image.open(io.BytesIO(response))
    phone = pytesseract.image_to_string(image_stream)
    print(phone)


if __name__ == '__main__':
    main()
