# coding:utf-8
"""
Name : demo1.py
Author  : Mark
Contect : hongming666@outlook.com
Time    : 2022/6/28 18:47
Desc:
"""
import requests
from lxml import etree
from pyquery import PyQuery

class Login(object):
    def __init__(self):
        self.headers = {
            'referer': 'https://github.com/',
            'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36',
        }
        self.login_url = 'https://github.com/login'
        self.post_url = 'https://github.com/session'
        self.logined_url = 'https://github.com/settings/profile'

        self.session = requests.session()

    def token(self):
        response = self.session.get(self.login_url, headers=self.headers)
        selector = etree.HTML(response.text)
        _token = selector.xpath('//*[@id="login"]/div[4]/form/input[1]/@value')
        timestamp = selector.xpath('//*[@id="login"]/div[4]/form/div/input[10]/@value')
        timestamp_secret = selector.xpath('//*[@id="login"]/div[4]/form/div/input[11]/@value')
        print(timestamp, _token, timestamp_secret)
        return {'_token' :_token, 'timestamp':timestamp, 'timestamp_secret':timestamp_secret}

    def profile(self, html):
        """

        :param html: profile页内容
        """
        selector = etree.HTML(html)
        name = selector.xpath('//*[@id="user_profile_name"]/div/text()')
        company = selector.xpath('//*[@id="user_profile_company"]/div/text()')
        print(name, company)

    def login(self, email, password):
        """

        :param email: 邮箱名
        :param password: 密码
        """
        data = self.token()
        post_data = {
            'commit': 'Sign in',
            'authenticity_token': data['_token'],
            'login': email,
            'password':password,
            'trusted_device':'',
            'webauthn-support': 'supported',
            'webauthn-iuvpaa-support': 'unsupported',
            'return_to': 'https://github.com/login',
            'allow_signup':'',
            'client_id':'',
            'integration':'',
            'required_field_71c7':'',
            'timestamp': data['timestamp'],
            'timestamp_secret': data['timestamp_secret']
        }
        response = self.session.post(self.post_url, data=post_data, headers=self.headers)
        if response.status_code == 200:
            print(response.text)

        responses = self.session.get(self.logined_url, headers=self.headers)
        if responses.status_code == 200:
            print(responses.text)
            self.profile(responses.text)


if __name__ == '__main__':
    login = Login()
    login.login(email='ming-666-ming', password='qwe13672Q')