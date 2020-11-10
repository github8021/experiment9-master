# -*- coding: utf-8 -*-
"""
-------------------------------------------------
# @Project  :experiment9
# @File     :requests_demo
# @Date     :2020/10/28 10:26
# @Author   :施嘉伟
# @Email    :1138128021@qq.com
# @Software :PyCharm
-------------------------------------------------
"""
import requests

headers = {
    'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36 Edg/85.0.564.41"}
response = requests.get("http://www.baidu.com", headers=headers)
html = response.text
# 获得文本
print(html)
# 获得编码
print(response.encoding)
# 获得字节内容
print(response.content)
# 获得响应码
print(response.status_code)
# 获得响应头
print(response.headers)
