import requests
import os
from bs4 import BeautifulSoup


class Reborn():
    def __init__(self):
        self.api_url = 'http://www.migudm.cn/opus/webQueryWatchOpusInfo.html'
        self.headers = {
            'User-Agent': "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"
        }

    def request(self, url):  ##这个函数获取网页的response 然后返回
        content = requests.get(url, headers=self.headers)
        return content

    def mkdir(self, path):  ##这个函数创建文件夹
        path = path.strip()
        isExists = os.path.exists(os.path.join("D:\\家庭教师", path))
        if not isExists:
            os.makedirs(os.path.join("D:\\家庭教师", path))
            os.chdir(os.path.join("D:\\家庭教师", path))  ##切换到目录
            return True
        else:
            return False

    '''
    咪咕动漫爬取 1-399话
    '''
    def download399(self):
        index = 1
        while (index < 400):
            data = {
                'hwOpusId': '001000008448',
                '000001662489': '000001662489',
                'index': index,
                'opusType': '2'
            }
            file_path = "第" + str(index) + "话"
            print("开始下载" + file_path)
            self.mkdir(file_path)
            response = requests.post(self.api_url, data)
            if response.status_code == 200:
                data = response.json()
                for a in data['data']['jpgList']:
                    file_name = a['fileName']
                    img_url = a['url']
                    print(file_name, img_url)
                    img = self.request(img_url)
                    f = open(file_name, 'ab')
                    f.write(img.content)
                    f.close()
            index = index + 1

    '''
    土豪漫画爬取400 -409话
    '''
    def download409(self):

        html_url = "https://www.tohomh123.com/gutingjiaoshi/"
        soup = BeautifulSoup(self.request(html_url).text, 'lxml')
        button = soup.find('input', id='sendbutton')
        print(button.get('data-id'))
        a_list = soup.find('ul', id='detail-list-select-1').find_all('a')
        for a in a_list:
            content = a.get_text().split('话')
            catalog = content[0]
            iid = content[1].replace('（','').replace('P）','').replace('(完结篇)','')
            href = a['href']
            sid = href[-7:-5]
            print(catalog,sid,iid, href)
            if(int(catalog) >= 400):
                self.downlodiid(catalog, sid,int(iid))


    def downlodiid(self,catalog,sid,iid):
        api_url = "https://www.tohomh123.com/action/play/read"
        id = 1
        file_path = "第" + catalog + "话"
        print("开始下载" + file_path,catalog,sid,iid)
        self.mkdir(file_path)
        while (id <= iid):
            data = {
                'did': '1979',
                'sid': sid,
                'iid': id,
                'tmp': '0.7514127654722624'
            }
            response = requests.get(api_url, params=data, headers=self.headers)
            if response.status_code == 200:
                data = response.json()
                img_url = data['Code']
                img = self.request(img_url)
                file_name = img_url[-8:]
                f = open(file_name, 'ab')
                f.write(img.content)
                f.close()
            else:
                print("请求出错")
            id = id + 1

if __name__ == '__main__':
    migudm = Migudm()
    migudm.download399()
