#coding:utf-8
from bs4 import BeautifulSoup
import requests,re,urllib,time

url = 'http://www.budejie.com/video/'

def get_page(url,data=None):

    hd = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:51.0) Gecko/20100101 Firefox/51.0'}
    wb_data = requests.get(url,headers=hd)
    soup = BeautifulSoup(wb_data.text,'html.parser')
    lists = soup.findAll('a', href=re.compile('http://svideo.spriteapp.com/video/2017/(.*?)\.mp4'))
    a = 0
    for i in lists:
        a += 1
        url_href = i.get('href')
        print 'num' + str(a) + 'video'
        urllib.urlretrieve(url_href, "" + str(time.time()) + ".mp4")
def get_more_pages(start,end):
    for one in range(start,end):
        get_page(url+str(one))
        time.sleep(2)


get_more_pages(1,5)
