import requests
import os
import re
import json
from bs4 import BeautifulSoup


class Act():


    def __init__(self):
        self.headers = {
            'User-Agent': "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"
        }
        self.domain = 'https://www.gufengmh8.com/'
        self.img_domain= 'https://res.gufengmh8.com/' #'http://res.mhkan.com/'

    def request(self, url):  ##这个函数获取网页的response 然后返回
        content = requests.get(url, headers=self.headers)
        content.encoding = 'utf-8'
        return content

    def save(self,name, img_url):  ##这个函数保存图片
        if name == "" :
            name = img_url[-9:-4]
        img = self.request(img_url)
        f = open(name + '.jpg', 'ab')
        f.write(img.content)
        f.close()

    def mkdir(self, path):  ##这个函数创建文件夹
        path = path.strip()
        isExists = os.path.exists(os.path.join("D:\\comic\\钻石王牌act2", path))
        if not isExists:
            os.makedirs(os.path.join("D:\\comic\\钻石王牌act2", path))
            os.chdir(os.path.join("D:\\comic\\钻石王牌act2", path))  ##切换到目录
            return True
        else:
            return False
    '''
    爬取漫画
      https://www.mhkan.com/manhua/zuanshiwangpait2/
      https://www.gufengmh8.com/manhua/zuanshiwangpait2/#chapters
    '''

    def download(self,url):

        soup = BeautifulSoup(self.request(url).text, 'lxml')
        list = soup.find('ul', id='chapter-list-1').find_all('a')
        for a in list:
            span_tag = a.span.extract()
            self.mkdir(span_tag.get_text())
            href = a['href']  # 取出a标签的href 属性
            chapter = BeautifulSoup(self.request(self.domain+href).text, 'lxml')
            self.getChapterImage(chapter)
        print("下载完成")


    '''
    www.gufengmh8.com下载单章节,self.img_domain = 'https://res.gufengmh8.com/'
    '''
    def downloadOne(self,dir_name,url):
        self.mkdir(dir_name)
        chapter = BeautifulSoup(self.request(url).text, 'lxml')
        self.getChapterImage(chapter)

    def getChapterImage(self,chapter):
        for script in chapter.find_all("script", {"src": False}):
            chapter_path=""
            searchObj = re.search(r'var chapterImages = (.*?);$', script.text)
            if searchObj:
                data = searchObj.group(1)
                img_name_list = data.split(";")[0]
                list = json.loads(img_name_list)
                searchPath = re.search(r'var chapterPath = (.*?);$', script.text)
                if searchPath:
                    data = searchPath.group(1)
                    chapter_path = data.split(";")[0]
                    chapter_path = json.loads(chapter_path)
                print(chapter_path, img_name_list)
                for index, img in enumerate(list):
                    img_url = self.img_domain+chapter_path+img
                    name = str(index+1)
                    self.save(name,img_url)

if __name__ == '__main__':
    act= Act()
    # act.downloadOne('第170话 无数次',"https://www.gufengmh8.com/manhua/zuanshiwangpait2/941344.html")
    act.download("https://www.gufengmh8.com/manhua/zuanshiwangpait2/#chapters")