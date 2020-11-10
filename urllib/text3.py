# -*- coding: utf-8 -*-
"""
-------------------------------------------------
# @Project  :experiment9
# @File     :text3
# @Date     :2020/10/28 09:56
# @Author   :施嘉伟
# @Email    :1138128021@qq.com
# @Software :PyCharm
-------------------------------------------------
"""
import urllib.request
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

urllib.request.urlretrieve("http://www.sohu.com", "sohu.html")
urllib.request.urlretrieve("https://ss1.bdstatic.com/70cFuXSh_Q1YnxGkpoWK1HF6hhy/it/u=2022165842,3988576039&fm=26&gp=0.jpg","老虎.jpg")