# -*- coding: utf-8 -*-
"""
-------------------------------------------------
# @Project  :experiment9
# @File     :muKe
# @Date     :2020/10/28 10:39
# @Author   :施嘉伟
# @Email    :1138128021@qq.com
# @Software :PyCharm
-------------------------------------------------
"""
import requests

# 发出请求，获得响应
# https://www.imooc.com/search/?words=Python&type=course
kw = input("请输入课程名称:")
url = "https://www.imooc.com/search/?type=course&words=" + kw
# 伪装成浏览器
headers = {
    'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36 Edg/85.0.564.41"}
response = requests.get(url, headers=headers)
html = response.text

# 存放到网页文件里
with open("mooc.html", 'w', encoding="utf-8")as fp:
    fp.write(html)
