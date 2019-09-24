import requests
import os
import random
import itertools
from bs4 import BeautifulSoup


def main(url):
    # http://www.lottery.gov.cn/historykj/history.jspx?_ltype=dlt 中国体彩网
    headers = {
        'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"}  ##浏览器请求头（大部分网站没有这个请求头会报错、请务必加上哦）
    start_html = requests.get(url,
                              headers=headers)  ##使用requests中的get方法来获取all_url(就是：http://www.mzitu.com/all这个地址)的内容 headers为上面设置的请求头、请务必参考requests官方文档解释
    start_html.encoding = 'utf-8'
    print(start_html.text)  ##打印出start_html (请注意，concent是二进制的数据，一般用于下载图片、视频、音频、等多媒体内容是才使用concent, 对于打印网页内容请使用text)
    soup = BeautifulSoup(start_html.text, 'lxml')
    dataList = soup.find('tbody', id='tdata').find_all('tr')
    print(len(dataList))
    for item in dataList:
        tdList = item.find_all('td')
        print('期号：', tdList[0].text, '开奖日期：', tdList[-1].text, '开奖号码：前区：', tdList[1].text, '\t', tdList[2].text, '\t',
              tdList[3].text, '\t', tdList[4].text, '\t', tdList[5].text, '后区：', tdList[6].text, '\t', tdList[7].text)


def generator(red_remove, blue_remove):
    print(sorted(red_remove))
    a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30,
         31, 32, 33, 34, 35]
    b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    for m in red_remove:
        a.remove(m)
    print(a)
    for n in blue_remove:
        b.remove(n)
    print(b)
    red = (list(itertools.combinations(a, 5)))
    red_num = len(red)
    blue = list(itertools.combinations(b, 2))
    blue_num = len(blue)
    print('前区组合：', red_num, '后区组合：', blue_num, '总个数：', red_num * blue_num)
    redIndex = random.randint(0, red_num)
    blueIndex = random.randint(0, blue_num)
    print('生成号码：前区：', red[redIndex], '后区号码：', blue[blueIndex])


if __name__ == '__main__':
    url = "http://datachart.500.com/dlt/history/newinc/history.php?start=19001&end=19111"
    main(url)
    generator([6,15,20,23,27,1,2,5,35,25,9,19,22,26,12], [8,10,2,12,11,1])
