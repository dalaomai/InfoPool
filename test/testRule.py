#testRule.py



import unittest
import datetime
from common.Rule import Rule
from common.Message import Message

class TestRule(unittest.TestCase):

    def testBaseProperty(self):
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
        self.assertEqual(rule.webName,"佛山市人民政府")
        self.assertEqual(rule.webUrl,"http://www.foshan.gov.cn/zwgk/zwdt/jryw/")
        self.assertEqual(rule.ruleModel,"regular")
        self.assertEqual(rule.rulePattern,r'<li [\s\S]*?([0-9]{4}-[0-9]{2}-[0-9]{2})[\s\S]*?href="([\s\S]*?)"[\s\S]*?title="([\s\S]*?)" >')
        self.assertEqual(rule.titlePosition,"2")
        self.assertEqual(rule.hrefPosition,"1")
        self.assertEqual(rule.timePosition,"0")
        self.assertEqual(rule.isEffect,1)

        self.assertNotEqual(rule.subscribeUpdateTime,None)
        self.assertEqual(rule.subscribeIsPush,None)
        self.assertEqual(rule.subscribeLastPushTime,None)
        return

    def testBaseMethod(self):
        nowTime = datetime.datetime.now()
        rule = Rule(id = 1,
                    webName="佛山市科学技术局",
                    webUrl = "http://www.fskw.gov.cn/tzgg/",
                    ruleModel = "regular",
                    rulePattern=r'<li><span>[\s\S]*?([0-9]{4}-[0-9]{2}-[0-9]{2})[\s\S]*?href="([\s\S]*?)"[\s\S]*?title="([\s\S]*?)">[\s\S]*?</li>',
                    titlePosition="2",
                    hrefPosition = "1",
                    timePosition="0",
                    isEffect = 1
                    )
        msg = Message("title","href",nowTime,1)

        self.assertRaises(AssertionError,rule.addMessage,1)
        rule.addMessage(msg)
        msg = rule.getMessages()
        self.assertEqual(msg[0].title,"title")
        rule.removeMessage(msg[0])
        msg = rule.getMessages()
        self.assertEqual(len(msg),0)
        msg = Message("title","href",nowTime,1)
        rule.addMessage(msg)
        rule.removeMessageById(1)
        msg = rule.getMessages()
        self.assertEqual(len(msg),0)