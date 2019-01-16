#testHtmlParser.py


import unittest
from common.HtmlParser import HtmlParser
from common.HtmlDownload import HtmlDownload
from common.Rule import Rule

class TestHtmlParser(unittest.TestCase):

    def testParser(self):
        parser = HtmlParser()
        rule = Rule(id = 1,
            webName="佛山市人民政府",
            webUrl = "http://www.foshan.gov.cn/zwgk/zwdt/jryw/",
            ruleModel = "regular",
            rulePattern=r'<li [\s\S]*?([0-9]{4}-[0-9]{2}-[0-9]{2})[\s\S]*?href="([\s\S]*?)"[\s\S]*?title="([\s\S]*?)" >',
            titlePosition="2",
            hrefPosition = "1",
            timePosition="0",
            isEffect = 1
            )
        html = HtmlDownload.download(rule.webUrl)
        msgs = parser.RegularPraser(html,rule)
        self.assertNotEqual(len(msgs),0)
        msgs = parser.parse(html,rule)
        self.assertNotEqual(len(msgs),0)
        msgs,matchs = parser.parseForAPI(html,rule)
        self.assertNotEqual(len(msgs),0)
        self.assertNotEqual(len(matchs),0)

        msgs = parser.parse('',rule)
        self.assertEqual(len(msgs),0)
        pass

