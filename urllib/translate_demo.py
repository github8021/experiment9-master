# -*- coding: utf-8 -*-
"""
-------------------------------------------------
# @Project  :experiment9
# @File     :translate_demo
# @Date     :2020/10/28 11:31
# @Author   :施嘉伟
# @Email    :1138128021@qq.com
# @Software :PyCharm
-------------------------------------------------
"""
import requests
while True:
    inputword = input('请输入你要查询的英语单词：\n')
    url = 'https://fanyi.baidu.com/sug'
    headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'}
    data = {'kw': '{}'.format(inputword)}
    response = requests.post(url=url, data=data, headers=headers).json()
    data = response.get('data')
    print(data)
    for i in data:
        words = i.get('k')
        fanyi = i.get('v')
        fanyi_danci = words + ':' + fanyi + '\n'
        print(fanyi_danci)
        with open('danci.txt', 'a', encoding='utf-8')as fp:
            fp.write(fanyi_danci)
