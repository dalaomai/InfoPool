#infoCrawl.py
from common import Rule,Message,HtmlParser,HtmlDownload
from db import DataBaseOperate
from util import logger

class InfoCrawl(object):

    def __init__(self):
        '''

        '''
        self.rules = None
        self.messages = None
        self.dbo = DataBaseOperate()
        self.htmlDownload = HtmlDownload()
        self.htmlParser = HtmlParser()

    def run(self):
        rules = self.dbo.getAllRules()
        logger.info("get " + str(len(rules)) + " rules to update message")
        rule = Rule()
        for rule in rules:
            html = self.htmlDownload.download(rule.webUrl,rule.webModel)
            if html == -1:
                continue
            messages = self.htmlParser.parse(html,rule)
            for msg in messages:
                rule.addMessage(msg)
            result = self.dbo.saveMessagesFromRule(rule)
            logger.info(rule.webUrl + " update " + str(result) + " messages")

if __name__=="__main__":
    ic = InfoCrawl()
    ic.run()
