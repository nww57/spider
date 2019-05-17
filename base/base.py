import requests
import os
from bs4 import BeautifulSoup


headers = {
            'User-Agent': "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"
        }

def request(url):
    content = requests.get(url, headers=headers)
    return content