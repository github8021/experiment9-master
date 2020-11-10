# -*- coding: utf-8 -*-
"""
-------------------------------------------------
# @Project  :experiment9
# @File     :text1
# @Date     :2020/10/28 09:13
# @Author   :施嘉伟
# @Email    :1138128021@qq.com
# @Software :PyCharm
-------------------------------------------------
"""
import urllib.request
# 发出请求，得到响应
response=urllib.request.urlopen("http://www.gengdan.cn/")
print(response.geturl())
html = response.read().decode("UTF-8")
with open("bgdGW.html",'w',encoding="utf-8")as fp:
    fp.write(html)
print(response.geturl())
