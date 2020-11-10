# -*- coding: utf-8 -*-
"""
-------------------------------------------------
# @Project  :experiment9
# @File     :hello
# @Date     :2020/10/28 11:43
# @Author   :施嘉伟
# @Email    :1138128021@qq.com
# @Software :PyCharm
-------------------------------------------------
"""
import requests

words = set()
while True:
    a = input("请输入您要查询的英语单词，按0结束:")
    if (a == '0'):
        break
    words.add(a)

for i in words:
    url = 'https://fanyi.baidu.com/sug'
    headers = {
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'}
    data = {'kw': '{}'.format(i)}
    response = requests.post(url=url, data=data, headers=headers).json()
    data = response.get('data')
    for i in data:
        words = i.get('k')
        fanyi = i.get('v')
        fanyi_danci = words + ':' + fanyi + '\n'
        print(fanyi_danci)
        with open('words.txt', 'w', encoding='utf-8')as fp:
            fp.write(fanyi_danci)
