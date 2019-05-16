#testHtmlDownload.py
import unittest
from common.HtmlDownload import HtmlDownload
from common.Rule import Rule
from datetime import datetime

class TestHtmlDownload(unittest.TestCase):
    nowTime = datetime.now()
    rule = Rule(id = 1,
                    webName="baidu",
                    webUrl = "https://www.baidu.com/",
                    webModel = "normal",
                    ruleModel = "regular",
                    rulePattern=r'<li [\s\S]*?([0-9]{4}-[0-9]{2}-[0-9]{2})[\s\S]*?href="([\s\S]*?)"[\s\S]*?title="([\s\S]*?)" >',
                    titlePosition="2",
                    hrefPosition = "1",
                    timePosition="0",
                    isEffect = 1,
                    updateTime = nowTime
                    )

    def testBaseProperty(self):
        self.rule.webUrl = "https://www.baidu.com/"
        htmlDownload = HtmlDownload()
        r = htmlDownload.download(self.rule.webUrl,self.rule.webModel)
        self.assertNotEqual(r,-1)
        self.rule.webUrl = 'www.baidu.com'
        r = htmlDownload.download(self.rule.webUrl,self.rule.webModel)
        self.assertEqual(r,-1)

        self.rule.webUrl = r'http://paperpost.people.com.cn/all-rmrb-\Y-\m-\d.html'
        self.rule.webModel = 'date'
        r = htmlDownload.download(self.rule.webUrl,self.rule.webModel)
        self.assertNotEqual(r,-1)

