import requests
import os
import random
import itertools
from bs4 import BeautifulSoup


def main(url):
    # http://www.lottery.gov.cn/historykj/history.jspx?_ltype=dlt 中国体彩网
    # https://kaijiang.500.com/dlt.shtml 500彩票
    headers = {
        'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"}  ##浏览器请求头（大部分网站没有这个请求头会报错、请务必加上哦）
    start_html = requests.get(url,
                              headers=headers)  ##使用requests中的get方法来获取all_url(就是：http://www.mzitu.com/all这个地址)的内容 headers为上面设置的请求头、请务必参考requests官方文档解释
    start_html.encoding = 'utf-8'
    ## print(start_html.text)  ##打印出start_html (请注意，concent是二进制的数据，一般用于下载图片、视频、音频、等多媒体内容是才使用concent, 对于打印网页内容请使用text)
    soup = BeautifulSoup(start_html.text, 'lxml')
    dataList = soup.find('tbody', id='tdata').find_all('tr')
    print(len(dataList))
    for item in dataList:
        tdList = item.find_all('td')
        print('期号：', tdList[0].text, '开奖日期：', tdList[-1].text, '开奖号码：前区：', tdList[1].text, '\t', tdList[2].text, '\t',
              tdList[3].text, '\t', tdList[4].text, '\t', tdList[5].text, '后区：', tdList[6].text, '\t', tdList[7].text,'\t','奖池奖金（元）：',tdList[8].text)


def generator(red_remove, blue_remove):
    red_remove = list(set(red_remove))
    blue_remove = list(set(blue_remove))
    print('前区杀号：', sorted(red_remove), '后区杀号：',sorted(blue_remove))
    a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30,
         31, 32, 33, 34, 35]
    b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    for m in red_remove:
        a.remove(m)
    for n in blue_remove:
        b.remove(n)
    print('前区剩余号码：', sorted(a), '后区剩余号码：', sorted(b))
    red = (list(itertools.combinations(a, 5)))
    red_num = len(red)
    blue = list(itertools.combinations(b, 2))
    print('后期剩余组合：', blue)
    blue_num = len(blue)

    m=[]
    while(len(m)<5):
        x = random.randint(0,red_num-1)
        if x not in m:
            m.append(x)
    n=[]
    while(len(n)<5):
        z = random.randint(0,blue_num-1)
        if z not in n:
            n.append(z)
    print(m)
    print(n)

    print('前区组合：', red_num, '后区组合：', blue_num, '总个数：', red_num * blue_num)
    print('随机5组：')
    for inx, val in enumerate(m):
        print(red[val],blue[n[inx]])


if __name__ == '__main__':
    url = "http://datachart.500.com/dlt/history/newinc/history.php?start=19001&end=19136"
    generator([10,13,18,23,30,20,21,25,34,35,5,9,16,18,30,14,7,17,26,27], [2,3,4,7,8,11])
    main(url)