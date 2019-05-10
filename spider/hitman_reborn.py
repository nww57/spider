import requests
import os
from bs4 import BeautifulSoup


class Migudm():
    '''
    咪咕动漫爬取 1-399话
    '''
    def __init__(self):
        self.api_url = 'http://www.migudm.cn/opus/webQueryWatchOpusInfo.html'
        self.headers = {
            'User-Agent': "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"}

    def request(self, url):  ##这个函数获取网页的response 然后返回
        content = requests.get(url, headers=self.headers)
        return content

    def mkdir(self, path):  ##这个函数创建文件夹
        path = path.strip()
        isExists = os.path.exists(os.path.join("D:\家庭教师", path))
        if not isExists:
            os.makedirs(os.path.join("D:\\家庭教师", path))
            os.chdir(os.path.join("D:\\家庭教师", path))  ##切换到目录
            return True
        else:
            return False

    def download(self):
        index = 1
        while (index < 400 ) :
            data = {
                'hwOpusId': '001000008448',
                '000001662489': '000001662489',
                'index': index,
                'opusType': '2'
            }
            file_path = "第"+str(index)+"话"
            print("开始下载"+file_path)
            self.mkdir(file_path)
            response = requests.post(self.api_url,data)
            if response.status_code == 200 :
                data = response.json()
                for a in data['data']['jpgList']:
                    file_name = a['fileName']
                    img_url = a['url']
                    print(file_name,img_url)
                    img = self.request(img_url)
                    f = open(file_name, 'ab')
                    f.write(img.content)
                    f.close()
            index = index +1




if __name__ == '__main__':
    migudm = Migudm()
    migudm.download()