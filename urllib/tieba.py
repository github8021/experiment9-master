# -*- coding: utf-8 -*-
"""
-------------------------------------------------
# @Project  :experiment9
# @File     :tieba
# @Date     :2020/10/28 10:49
# @Author   :施嘉伟
# @Email    :1138128021@qq.com
# @Software :PyCharm
-------------------------------------------------
"""
# https://tieba.baidu.com/f?ie=utf-8&kw=%E5%8C%97%E4%BA%AC%E5%B7%A5%E4%B8%9A%E5%A4%A7%E5%AD%A6%E8%80%BF%E4%B8%B9%E5%AD%A6%E9%99%A2&fr=search
import requests
import time
kw = input("请输入贴吧名称:")
url = "https://tieba.baidu.com/f?ie=utf-8&fr=search&kw=" + kw
headers = {
    'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36 Edg/85.0.564.41"}
response = requests.get(url, headers=headers)
html = response.text

# 存放到网页文件里
with open("tieba第一页.html", 'w', encoding="utf-8")as fp:
    fp.write(html)

for i in range(50,15560,50):
    url = "https://tieba.baidu.com/f?ie=utf-8&fr=search&kw=" + kw+"&pn="+str(i)
    response = requests.get(url, headers=headers)
    html = response.text

    # 存放到网页文件里
    with open("tieba/tieba第"+str(i)+"页.html", 'w', encoding="utf-8")as fp:
        fp.write(html)
    time.sleep(0.5)

