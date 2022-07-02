# coding:utf-8
"""
Name : canvas.py
Author  : Mark
Contect : hongming666@outlook.com
Time    : 2022/7/2 15:31
Desc:   canvas slide verify code
"""

from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from PIL import Image, ImageChops


def main():
    """
    主函数
    """
    url = "http://www.porters.vip/captcha/jigsawCanvas.html"
    browser = webdriver.Chrome(executable_path='../resource/chromedriver.exe')
    # 最大等待时间
    WebDriverWait(browser, 10)
    browser.get(url)
    # 定位滑块
    jigsawCircle = browser.find_element(By.ID, 'jigsawCircle')
    # 定位背景图片
    jigsawCanvas = browser.find_element(By.ID, 'jigsawCanvas')
    jigsawCanvas.screenshot('before.png')
    action = webdriver.ActionChains(browser)
    # 点击并保持不松开
    action.click_and_hold(jigsawCircle).perform()
    # 执行JavaScript代码隐藏圆角矩阵的HTML代码
    scripts = """"
        var missblock = document.getElementById('missblock');
        missblock.style['visibility'] = 'hidden';
    """
    browser.execute_script(scripts)
    jigsawCanvas.screenshot('after.png')

    # 打开对比的图片
    image_a = Image.open('after.png')
    image_b = Image.open('before.png')

    # 使用 ImageChops 模块中的difference()方法对比图片像素的不同，
    diff = ImageChops.difference(image_b, image_a)
    # 获取图片差异位置的坐标
    diff_position = diff.getbbox()
    print(diff_position)

    position_x = diff_position[0]
    # 设置移动距离
    action.move_by_offset(int(position_x) - 10, 0)
    # 松开鼠标
    action.release()
    browser.close()


if __name__ == '__main__':
    main()