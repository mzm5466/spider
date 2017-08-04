# coding:utf-8
from bs4 import BeautifulSoup
import requests, re, urllib, time, datetime
import threading
lista = []


def get_page(num):
    url = 'http://desk.zol.com.cn/showpic/1920x1080_' +str(int(1000)+int(num)) + '_6.html'
    hd = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:51.0) Gecko/20100101 Firefox/51.0'}
    wb_data = requests.get(url, headers=hd)
    soup = BeautifulSoup(wb_data.text, 'html.parser')
    images = soup.find("img", {"src": re.compile("http://desk.fd.zol-img.com.cn/(.*?)\.jpg")})
    imglink=images.get('src')
    urllib.urlretrieve(imglink, "img" + str(num) + ".jpg")
    print "已下载第"+str(num)+"张图片！"
def pubStart():
    """
           开始消息推送
           """
    print "开始时间：" + str(time.ctime())
    starttime = datetime.datetime.now()
    for i in xrange(77888,87888):
        lista.append(str(i))

    # 线程池
    threads = []

    print "程序开始运行%s" % datetime.datetime.now()
    for speed in lista:
        th = threading.Thread(target=get_page, args=(speed,))
        th.setDaemon(True)  # 守护进程
        th.start()
        threads.append(th)
        if (int(speed) % 100 == 0):  # 速度控制点
            time.sleep(5)
    # 等待线程运行完毕
    for th in threads:
        th.join()
        time.sleep(0.01)
    endtime = datetime.datetime.now()
    print "结束时间：" + str(time.ctime())
    print "耗时：" + str(endtime - starttime)


pubStart()
