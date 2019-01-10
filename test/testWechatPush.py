#testWechatPush.py
from common import Message,Rule,User
from bin import WechatPush
import unittest
from datetime import datetime

class TestWechatPush(unittest.TestCase):

    user = User(userName='dalaomai',
                password='admin',
                wechatId='MAIZHILING',
                wechatName='dalaomai')
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
    msg = Message("test","http://www.foshan.gov.cn/zwgk/zwdt/jryw/","2019-1-8")
    rule.addMessage(msg)
    rule.addMessage(msg)
    user.addRule(rule)
    user.addRule(rule)

    def testBaseMethod(self):
        wechatPush = WechatPush()
        self.assertEqual(wechatPush.getAccessToken(),0)
        text = wechatPush.structureMessageTextByMessage(self.msg)
        self.assertEqual(wechatPush.sendMessages(self.user,text),0)


        self.assertEqual( wechatPush.push(),0)
        return
