# coding:utf-8
"""
Name : slider.py
Author  : Mark
Contect : hongming666@outlook.com
Time    : 2022/7/2 8:42
Desc:   slide verify code
"""

"""

                                <div class="missblock" id="missblock" style="background-image: url(&quot;images/0.jpg&quot;);"></div>
                                <div class="targetblock" id="targetblock"></div>
                            </div>
                            <div class="jigsawTrack" id="jigsawTrack">
                                <span class="jigsawCircle" id="jigsawCircle"></span>
                           
"""
"""
   
                                <div class="missblock" id="missblock" style="background-image: url(&quot;images/0.jpg&quot;); left: 10px; display: block; top: 53.2136px; background-position: -117.241px -34.2136px;"></div>
                                <div class="targetblock" id="targetblock" style="display: block; left: 129.908px; top: 53.2136px;"></div>
                            </div>
                            <div class="jigsawTrack" id="jigsawTrack">
                                <span class="jigsawCircle" id="jigsawCircle" style="left: 0px;"></span>
                           
"""

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from parsel import Selector
from selenium.webdriver.common.by import By
import re
def main():
    """
    滑动验证码校验
    """
    # 驱动Chrome打开滑动验证码示例页面
    url = "http://www.porters.vip/captcha/jigsaw.html"
    browser = webdriver.Chrome(executable_path='../resource/chromedriver.exe')
    WebDriverWait(browser, 10)
    browser.get(url=url)
    # 定位滑块
    jigsawCircle = browser.find_element(By.ID, "jigsawCircle")
    # 点击并保持不松开
    action = webdriver.ActionChains(browser)
    action.click_and_hold(jigsawCircle).perform()

    # 获取页面内容
    html = browser.page_source

    sel = Selector(html)
    # 获取圆角矩阵和缺口的css
    mbk_style= sel.css('#missblock::attr("style")').get()
    tar_style = sel.css('#targetblock::attr("style")').get()
    extract = lambda x:''.join(re.findall('left:(\d+|\d+.\d+)px', x))
    mbk_left = extract(mbk_style)
    tar_left = extract(tar_style)
    # 计算当前拼图验证码滑块所需移动的距离
    distance = float(tar_left) - float(mbk_left)
    action.move_by_offset(distance, 0)  # 设置滑动距离
    action.release()    # 松开鼠标
    browser.close()


if __name__ == '__main__':
    main()
