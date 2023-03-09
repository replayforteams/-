# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from lxml import html
import requests
# import urllib.request
# resp=urllib.request.urlopen('https://jira.auto.continental.cloud/browse/S202-872?filter=-2')
# html=resp.read()
# print(html)
#
# https://jira.auto.continental.cloud/browse/S202-872?filter=-2
import requests
from bs4 import BeautifulSoup


def getHTMLText(url):
    '''
    此函数用于获取网页的html文档
    '''
    try:
        # 获取服务器的响应内容，并设置最大请求时间为6秒
        res = requests.get(url, timeout=12)
        # 判断返回状态码是否为200
        res.raise_for_status()
        # 设置该html文档可能的编码
        res.encoding = res.apparent_encoding
        # 返回网页HTML代码
        return res.text
    except:
        return '产生异常'


def main():
    '''
    主函数
    '''
    # 目标网页，这个可以换成一个你喜欢的网站
    url = 'https://jira.auto.continental.cloud/browse/S202-872?filter=-2'

    demo = getHTMLText(url)

    # 解析HTML代码
    soup = BeautifulSoup(demo, 'html.parser')

    # 模糊搜索HTML代码的所有包含href属性的<a>标签
    a_labels = soup.find_all('a', attrs={'href': True})

    # 获取所有<a>标签中的href对应的值，即超链接
    for a in a_labels:
        print(a.get('href'))


main()