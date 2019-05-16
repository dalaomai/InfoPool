from common import HtmlDownload
import web
import json

class HtmlDownloadAPI(object):
    def __init__(self, *args, **kwargs):
        self.__msg = {
            'url':'',
            'html':''
            }
        self.htmlDownload = HtmlDownload()
        pass

    def GET(self):
        inputs = web.input(url='')
        self.__msg['url'] = inputs.url
        if self.__msg['url'] == '':
            self.__msg['html'] = -1
            return json.dumps(self.__msg)
        self.__msg['html'] = self.htmlDownload.download(self.__msg['url'],'normal')
        return json.dumps( self.__msg)

    def POST(self):
        return self.get()



