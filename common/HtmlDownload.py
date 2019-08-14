


from config import HtmlDownload_RETRY_TIME,HtmlDownload_TIMEOUT,HtmlDownload_get_header
from util import logger
from common.EscapeTool import EscapeTool
import re

import requests
import chardet
from datetime import datetime


class HtmlDownload():
    def __init__(self, *args, **kwargs):
        return

    def download(self,url,model="normal",**kwargs):
        if re.search('http',url) == None:
            url = 'http://' + url

        try:
            if model == "normal":
                return self.normalDownload(url)
            elif model == "date":
                if 'date' in kwargs.keys():
                    return self.dateDownload(url,kwargs['date'])
                else:
                    return self.dateDownload(url)
            else:
                logger.error("web model is not match")
                return -1
        except Exception as e:
            logger.error("download model has error : {}".format(e), exc_info=True)
        
        return -1

    @staticmethod
    def normalDownload(url):

        '''
        随机选择User-Agent，构成请求头
        备注：可增加，使用代理ip，进行下载
        '''

        count = 0  # 重试次数
        while count <= HtmlDownload_RETRY_TIME:
            try:
                r = requests.get(url=url, headers=HtmlDownload_get_header(), timeout=HtmlDownload_TIMEOUT)
                r.encoding = chardet.detect(r.content)['encoding']
            except Exception as e:
                count += 1
                if count > HtmlDownload_RETRY_TIME:
                    logger.debug("download " + url + " failed: {}".format(e),exc_info=True)
                    logger.warning("download " + url + " failed : {}".format(e))
                    return -1
                continue

            if (not r.ok):
                count += 1
            else:
                logger.info("download " + url + " successful")
                return r.text
        logger.warning("download " + url + " failed")
        return -1

    def dateDownload(self,url,nowTime = None):
        '''
        nowTime 默认值None即当前时间
        按日期更新的url
        
        '''
        if nowTime==None:
            nowTime = datetime.now()
        url = EscapeTool.replace(url,r'\Y',nowTime.strftime("%Y"))  #替换年
        url = EscapeTool.replace(url,r'\m',nowTime.strftime("%m"))  #替换月
        url = EscapeTool.replace(url,r'\d',nowTime.strftime("%d"))  #替换日
        
        return self.normalDownload(url)