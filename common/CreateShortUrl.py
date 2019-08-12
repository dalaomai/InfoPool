"""
生成短网址
"""
from config import BAIDU_TOKEN
import requests
import json

class CreateShortUrl:
    def create(self,longUrl):
        longUrl = self.__baidu(longUrl)
        return longUrl

    def __baidu(self,longUrl):
        url = 'https://dwz.cn/admin/v2/create'
        bodys = {'url':longUrl}
        headers = {'Content-Type':'content_type', 'Token':BAIDU_TOKEN}
        respone = requests.post(url=url,data=json.dumps(bodys),headers=headers)
        respone = json.loads(respone.text)
        return respone.get('ShortUrl',longUrl)

if __name__=='__main__':
    createShortUrl = CreateShortUrl()
    print(createShortUrl.create('https://cn.nytimes.com/culture/20190807/wod-boomerang/'))
