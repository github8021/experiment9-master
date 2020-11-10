# -*- coding: utf-8 -*-
"""
-------------------------------------------------
# @Project  :experiment9
# @File     :test
# @Date     :2020/11/1 14:27
# @Author   :施嘉伟
# @Email    :1138128021@qq.com
# @Software :PyCharm
-------------------------------------------------
"""
import requests
from bs4 import BeautifulSoup

# 读本地文件
html_file = open('soup_demo.html', 'r', encoding="utf-8")
html = html_file.read()
soup = BeautifulSoup(html, 'lxml')
# print(soup.p.string) # 耿丹学院
# print(soup.title.parent.name) # head
print(soup.a.name) # <a class="sister" href="http://example.com/1" id="link1">工学院、商学院</a>
print(soup.find('a'))
# '''
# [<a class="sister" href="http://example.com/1" id="link1">工学院、商
# 学院</a>,
# <a class="sister" href="http://example.com/2" id="link2">人文学院
# </a>]
# '''
# print(soup.find(id="link2")) # <a class="sister" href="http://example.com/2" id="link2">人文学院</a>
# print(soup.get_text())
