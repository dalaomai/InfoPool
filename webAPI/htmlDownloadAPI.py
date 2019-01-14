from common import HtmlDownload
import web
import json

class HtmlDownloadAPI(object):
    def __init__(self, *args, **kwargs):
        self.__msg = {
            'url':'',
            'html':''
            }
        pass

    def GET(self):
        inputs = web.input(url=None)
        self.__msg['url'] = inputs.url
        if self.__msg['url'] == None:
            return json.dumps(self.__msg)
        self.__msg['html'] = HtmlDownload.download(self.__msg['url'])
        return json.dumps( self.__msg)

    def POST(self):
        return self.get()



