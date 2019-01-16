#api.py
import web
import sys
from util import logger
from config import API_HOST
from webAPI import HtmlDownloadAPI,HtmlParserAPI

class API:
    def __init__(self):
        urls = (
            '/HtmlDownloadAPI','HtmlDownloadAPI',
             '/HtmlParserAPI','HtmlParserAPI'
            )
        sys.argv.append(API_HOST)
        self.__api = web.application(urls,globals())

    def run(self):
        self.__api.run()
        pass



if __name__ == '__main__':
    api = API()
    api.run()