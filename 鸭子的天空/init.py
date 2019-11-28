import base64
import requests
import os
import re
import json
from bs4 import BeautifulSoup


class Act:

    def getimagelist(self, image_data):
        return base64.b64decode(image_data)

    def __init__(self):
        self.headers = {
            'User-Agent': "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"
        }
        self.domain = 'https://www.manhuadb.com'
        self.img_domain = 'https://res.gufengmh8.com/'  # 'http://res.mhkan.com/'

    def request(self, url):  ##这个函数获取网页的response 然后返回
        content = requests.get(url, headers=self.headers)
        content.encoding = 'utf-8'
        return content

    def save(self, name, img_url):  ##这个函数保存图片
        if name == "":
            name = img_url[-9:-4]
        img = self.request(img_url)
        f = open(name + '.jpg', 'ab')
        f.write(img.content)
        f.close()

    def mkdir(self, path):  ##这个函数创建文件夹
        path = path.strip()
        isExists = os.path.exists(os.path.join("D:\\comic\\鸭子的天空", path))
        if not isExists:
            os.makedirs(os.path.join("D:\\comic\\鸭子的天空", path))
            os.chdir(os.path.join("D:\\comic\\鸭子的天空", path))  ##切换到目录
            return True
        else:
            os.chdir(os.path.join("D:\\comic\\鸭子的天空", path))  ##切换到目录
            return False

    def download(self, url):
        soup = BeautifulSoup(self.request(url).text, 'lxml')
        list = soup.find('ul', id='chapter-list-1').find_all('a')
        for a in list:
            span_tag = a.span.extract()
            self.mkdir(span_tag.get_text())
            href = a['href']  # 取出a标签的href 属性
            chapter = BeautifulSoup(self.request(self.domain + href).text, 'lxml')
            self.getChapterImage(chapter)
        print("下载完成")
    def download(self, url,id):
        soup = BeautifulSoup(self.request(url).text, 'lxml')
        list = soup.find('div', id=id).find('ol').find_all('a')
        for a in list:
            dir_name = a.get_text()
            self.mkdir(dir_name)
            href = a['href']  # 取出a标签的href 属性
            print(self.domain+href)
            chapter = BeautifulSoup(self.request(self.domain + href).text, 'lxml')
            self.getChapterImage(chapter)
        print("下载完成")

    def getChapterImage(self, chapter):

        vg_r_data = chapter.find('div',class_="vg-r-data")

        host = vg_r_data.get("data-host")
        img_pre = vg_r_data.get("data-img_pre")
        print(host,img_pre)
        for script in chapter.find_all("script", {"src": False}):
            searchObj = re.search(r'var img_data = (.*?);$', script.text)
            if searchObj:
                img_data = searchObj.group(1)
                print(img_data)
                img_list = self.getimagelist(img_data)
                img_list = str(img_list,'utf-8')
                img_list = json.loads(img_list)
                print(img_list)
                for img in img_list:
                    print(img['p'],img['img_webp'],img['img'])
                    img_url = host + img_pre + img['img_webp']
                    print(img_url)
                    file_name = "%03d" % img['p'] + '.webp'
                    print(file_name)
                    i = self.request(img_url)
                    f = open(file_name, 'ab')
                    f.write(i.content)
                    f.close()

if __name__ == '__main__':

    act = Act()
    chapter = BeautifulSoup(act.request("https://www.manhuadb.com/manhua/1472/1622_17204.html").text, 'lxml')
    # act.getChapterImage(chapter)
    act.download("https://www.manhuadb.com/manhua/1472","1622")