"""
工具集
"""
from config import BAIDU_TOKEN
import requests
import json
import time


#生成短网址
def createShortUrl(longUrl):
    longUrl = __baidu(longUrl)
    return longUrl

def __baidu(longUrl):
    url = 'https://dwz.cn/admin/v2/create'
    bodys = {'url':longUrl}
    headers = {'Content-Type':'content_type', 'Token':BAIDU_TOKEN}
    respone = requests.post(url=url,data=json.dumps(bodys),headers=headers)
    respone = json.loads(respone.text)
    return respone.get('ShortUrl',longUrl)


#倒计时输出进度条
def countDown(seconds,length=20):
    '''
    length:进度条长度
    '''
    for i in range(seconds):
        print("{} seconds left||".format(seconds-i),end='')
        timedLength = i*length//seconds
        for _ in range(timedLength):
            print("/",end='')
        for _ in range(length-timedLength):
            print('_',end='')
        print('||\r',end='')
        time.sleep(1)
    print('')
            

if __name__=='__main__':

    #print(createShortUrl('https://cn.nytimes.com/culture/20190807/wod-boomerang/'))

    countDown(20)

