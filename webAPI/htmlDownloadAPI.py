from common import HtmlDownload
import web
import json
from datetime import datetime

class HtmlDownloadAPI(object):
    def __init__(self, *args, **kwargs):

        self.__msg = {
            'webUrl':'',
            'html':'',
            'webModel':'',
            'date':''
            }
        self.htmlDownload = HtmlDownload()
        pass

    def GET(self):
        nowTime = datetime.now()
        inputs = web.input(url='',webModel='normal',date=nowTime.strftime(r'%Y-%m-%d'))
        self.__msg['webUrl'] = inputs.url
        self.__msg['webModel'] = inputs.webModel
        self.__msg['date'] = inputs.date

        if self.__msg['webUrl'] == '':
            self.__msg['html'] = -1
            return json.dumps(self.__msg)
        
        date = datetime.strptime(self.__msg['date'],r'%Y-%m-%d')
        self.__msg['html'] = self.htmlDownload.download(self.__msg['webUrl'],self.__msg['webModel'],date=date)
        return json.dumps( self.__msg)

    def POST(self):
        return self.get()



