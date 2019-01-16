


from config import HtmlDownload_RETRY_TIME,HtmlDownload_TIMEOUT,HtmlDownload_get_header
from util import logger

import requests
import chardet


class HtmlDownload():
    def __init__(self, *args, **kwargs):
        return

    @staticmethod
    def download(url):

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
                    logger.debug("download " + url + " failed",exc_info=True)
                    logger.warning("download " + url + " failed")
                    return -1
                continue

            if (not r.ok):
                count += 1
            else:
                logger.info("download " + url + " successful")
                return r.text
        logger.warning("download " + url + " failed")
        return -1

