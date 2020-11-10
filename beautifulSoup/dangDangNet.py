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
    # 根据临时保存的列表
    print('开始写入数据 ====> ' + str(item))
    # 写入txt文件，追加的方式，设置编码
    with open('dangdang.txt', 'a', encoding='UTF-8') as f:
        # json.dumps将字典转换为字符串，ensure_ascii是转换为中文
        f.write(json.dumps(item, ensure_ascii=False) + '\n')
        # 数据流关闭
        f.close()


# 请求当当网，当我们请求成功之后，拿到源代码
def main(page):
    # 获取当当网网址，自动拼接页码
    url = 'http://bang.dangdang.com/books/fivestars/01.00.00.00.00.00-recent30-0-0-1-' + str(page)
    # 跳转到子函数，进行爬虫，获取内容
    html = request_dangdang(url)
    # 跳转到子函数，进行对爬取内容的解析，封装数据
    items = parse_result(html)
    # 跳转到子函数，遍历列表，并把它写到文章中
    for item in items:
        write_item_to_file(item)


def request_dangdang(url):
    try:
        # 获取url，并进行爬虫
        response = requests.get(url)
        if response.status_code == 200:
            # 200状态码代表成功，返回正确文本
            return response.text
    except requests.RequestException:
        # 异常返回空值
        return None

# 拿到源代码了，就要对其解析，使用正则表达式获取我们想要的关键信息，获取到了之后我们封装一下数据
def parse_result(html):
    # 使用lxmlHTML解析器来构造BeautifulSoup对象
    soup = BeautifulSoup(html, 'lxml')
    # 创建空列表Items,用于存放所有有用的数据
    items = []
    # 双重循环，外循环遍历所有包含ul的class为'bang_list clearfix bang_list_mode'的标签
    for li_tag in soup.find_all('ul', {'class': 'bang_list clearfix bang_list_mode'}):
        # 内循环遍历所有li标签
        for div_tag in li_tag.find_all('li'):
            # 每次循环新建空列表item
            item = []
            # 获取num
            num = div_tag.find('div', class_='list_num').text
            # 获取书名
            name = div_tag.find('img').get('alt', '')
            # 获取推荐信息
            tuijian = div_tag.find("span", class_="tuijian").text
            # 获取作者名
            author = div_tag.findAll("div", class_="publisher_info")[0].text
            # 获取日期
            date = div_tag.findAll("div", class_="publisher_info")[1].find('span').text
            #获取出版社
            publisher = div_tag.findAll("div", class_="publisher_info")[1].find('a').text
            # 获取飙升榜
            biaosheng = div_tag.find("div", class_="biaosheng").find('span').text
            # 获取价格
            price_n = div_tag.find("span", class_="price_n").text
            # 依次追加到列表中
            item.append(num)
            item.append(name)
            item.append(tuijian)
            item.append(author)
            item.append(date)
            item.append(publisher)
            item.append(biaosheng)
            item.append(price_n)
            # 列表嵌套，完成数据临时保存
            items.append(item)
    return items


if __name__ == '__main__':
    # 从第一页开始，遍历25次，每次20个数据，刚好前500名
    for i in range(1, 26):
        main(i)