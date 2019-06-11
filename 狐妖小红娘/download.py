import requests
import os
import re
from bs4 import BeautifulSoup
import base64
import json

class Fox():


    def __init__(self):
        self.headers = {
            'User-Agent': "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"
        }

    def request(self, url):  ##这个函数获取网页的response 然后返回
        content = requests.get(url, headers=self.headers)
        return content

    def mkdir(self, path):  ##这个函数创建文件夹
        path = path.strip()
        isExists = os.path.exists(os.path.join("D:\\comic\\狐妖小红娘", path))
        if not isExists:
            os.makedirs(os.path.join("D:\\comic\\狐妖小红娘", path))
            os.chdir(os.path.join("D:\\comic\\狐妖小红娘", path))  ##切换到目录
            return True
        else:
            return False
    '''
    爬取漫画
    '''
    def download(self):

        html_url = "https://www.tohomh123.com/huyaoxiaogongniang/"
        soup = BeautifulSoup(self.request(html_url).text, 'lxml')
        button = soup.find('input', id='sendbutton')
        data_id = button.get('data-id')
        print(data_id)
        list = soup.find('ul', id='detail-list-select-1').find_all('a')
        name_list = []
        for a in list:
            span_tag = a.span.extract()
            name = a.get_text()
            name = name.replace('·','')
            pattern = re.compile(r'\d+')
            ca = pattern.findall(name)
            if name not in name_list and ca :
                name_list.append(name)
                href = a['href']
                sid = pattern.findall(href)[0]
                iid = span_tag.get_text().replace('（','').replace('P）','')
                print(name,sid,iid)
                self.getimg(data_id,name,sid,int(iid))


    def getimg(self,dataid,catalog,sid,iid):
        api_url = "https://www.tohomh123.com/action/play/read"
        id = 1
        print("开始下载:",catalog)
        self.mkdir(catalog)
        while (id <= iid):
            data = {
                'did': dataid,
                'sid': sid,
                'iid': id,
                'tmp': '0.16518382679913435'
            }
            response = requests.get(api_url, params=data, headers=self.headers)
            if response.status_code == 200:
                data = response.json()
                img_url = data['Code']
                img = self.request(img_url)
                file_name = img_url.spilit("")[-1]
                f = open(file_name, 'ab')
                f.write(img.content)
                f.close()
            else:
                print("请求出错")
            id = id + 1

if __name__ == '__main__':
   fox = Fox()
   html = fox.request("https://ac.qq.com/ComicView/index/id/518333/cid/2")
   print(html.text)
   b64_data = html.text.find("var DATA        = '{}'")
   print(b64_data)
