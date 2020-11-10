# -*- coding: utf-8 -*-
"""
-------------------------------------------------
# @Project  :experiment9
# @File     :dangDangNet
# @Date     :2020/11/1 14:34
# @Author   :施嘉伟
# @Email    :1138128021@qq.com
# @Software :PyCharm
-------------------------------------------------
"""
import requests
import json
import lxml

# 写到文件中
from bs4 import BeautifulSoup


def write_item_to_file(item):
    print('开始写入数据 ====> ' + str(item))
    with open('dangdang.txt', 'a', encoding='UTF-8') as f:
        # json.dumps将字典转换为字符串，ensure_ascii是转换为中文
        f.write(json.dumps(item, ensure_ascii=False) + '\n')
        f.close()


# 请求当当网，当我们请求成功之后，拿到源代码
def main(page):
    url = 'http://bang.dangdang.com/books/fivestars/01.00.00.00.00.00-recent30-0-0-1-' + str(page)
    html = request_dangdang(url)
    items = parse_result(html)
    for item in items:
        write_item_to_file(item)


def request_dangdang(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
    except requests.RequestException:
        return None

# 拿到源代码了，就要对其解析，使用正则表达式获取我们想要的关键信息，获取到了之后我们封装一下数据
def parse_result(html):
    soup = BeautifulSoup(html, 'lxml')
    items = []
    for li_tag in soup.find_all('ul', {'class': 'bang_list clearfix bang_list_mode'}):
        for div_tag in li_tag.find_all('li'):
            item = []
            num = div_tag.find('div', class_='list_num').text
            name = div_tag.find('img').get('alt', '')
            tuijian = div_tag.find("span", class_="tuijian").text
            author = div_tag.findAll("div", class_="publisher_info")[0].text
            date = div_tag.findAll("div", class_="publisher_info")[1].find('span').text
            publisher = div_tag.findAll("div", class_="publisher_info")[1].find('a').text
            biaosheng = div_tag.find("div", class_="biaosheng").find('span').text
            price_n = div_tag.find("span", class_="price_n").text
            item.append(num)
            item.append(name)
            item.append(tuijian)
            item.append(author)
            item.append(date)
            item.append(publisher)
            item.append(biaosheng)
            item.append(price_n)
            items.append(item)
    return items


if __name__ == '__main__':
    for i in range(1, 26):
        main(i)