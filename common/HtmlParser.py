#HtmlParser.py

import re
from datetime import datetime
from urllib import parse
from lxml import etree
from util import logger
from common import Message


class HtmlParser(object):

    def __init__(self):
        '''
        regular √
        xpath x
        '''
        pass

    def parse(self, html, rule):
        '''
        '''
        try:
            #匹配解析模式
            if rule.ruleModel == 'regular':
                result,_ = self.RegularPraser(html, rule)
                return result
            else:
                raise Exception("规则类型选择失败！")
        except Exception as e:
            logger.error("HtmlParser.parse",exc_info=True)
            return []
        pass

    def parseForAPI(self,html,rule):
        '''
        '''
        try:
            #匹配解析模式
            if rule.ruleModel == 'regular':
                return self.RegularPraser(html, rule)
            else:
                raise Exception("规则类型选择失败！")
        except Exception as e:
            logger.error("HtmlParser.parse",exc_info=True)
            return []
        pass

    def RegularPraser(self, html, rule):
        '''
        针对正则表达式进行解析
        '''
        msgs = []
        pattern = re.compile(rule.rulePattern)
        matchs = pattern.findall(str(html))
        logger.info("Parse " + rule.webUrl + " have " + str(len(matchs)) + " match")

        if matchs != None:
            for match in matchs:
                try:
                    title = match[int(rule.titlePosition)]
                    href = match[int(rule.hrefPosition)]
                    href = parse.urljoin(rule.webUrl,href)
                    time = datetime.now().strftime("%Y-%m-%d")
                    if int(rule.timePosition)!=-1:
                        time = match[int(rule.timePosition)]
                except Exception as e:
                    logger.error("HtmlParser.RegularPraser",exc_info=True)
                    continue
                msgs.append(Message(title,href,time))
        return msgs,matchs

    def XpathPraser(self, response, rule):
        '''
        针对xpath方式进行解析
        :param response:
        :param rule:

        :return:
        '''
        infolist = []
        root = etree.HTML(response)
        infos = root.xpath(rule['pattern'])

        for info in infos:
            try:
                title = info.xpath(rule['position']['title'])[0]
                href = info.xpath(rule['position']['href'])[0]
                time = info.xpath(rule['position']['time'])[0]
            except Exception as e:
                continue
            info = {'title':title,'href':href,'time':time}
            infolist.append(info)
        return infolist,infos









