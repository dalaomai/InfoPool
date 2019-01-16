#testUser.py

import unittest
from datetime import datetime
from common import User,Rule


class TestUser(unittest.TestCase):

    def testBaseProperty(self):
        nowTime = datetime.now()
        user = User(id=1,
                    userName="dalaomai",
                    password = "admin",
                    permission=1,
                    wechatId="wechatId",
                    wechatName="wechatName",
                    registerTime= nowTime,
                    phoneNumber = 18888888888,
                    emailAddress = "mai@dalaomai.cn",
                    updateTime=nowTime)
        self.assertEqual(user.id,1)
        self.assertEqual(user.userName,"dalaomai")
        self.assertEqual(user.verifyPassword("admin"),1)
        self.assertEqual(user.permission,1)
        self.assertEqual(user.wechatId,"wechatId")
        self.assertEqual(user.wechatName,"wechatName")
        self.assertEqual(user.registerTime,nowTime)
        self.assertEqual(user.phoneNumber,18888888888)
        self.assertEqual(user.emailAddress,"mai@dalaomai.cn")
        self.assertEqual(user.updateTime,nowTime)

        user = User()
        self.assertEqual(user.id,None)
        self.assertEqual(user.userName,None)
        self.assertEqual(user.verifyPassword("admin"),0)
        self.assertEqual(user.permission,None)
        self.assertEqual(user.wechatId,None)
        self.assertEqual(user.wechatName,None)
        self.assertEqual(user.registerTime,None)
        self.assertEqual(user.phoneNumber,None)
        self.assertEqual(user.emailAddress,None)
        self.assertNotEqual(user.updateTime,None)



        pass
    
    def testBaseMethod(self):
        nowTime = datetime.now()
        user = User(id=1,
                    userName="dalaomai",
                    password = "admin",
                    permission=1,
                    wechatId="wechatId",
                    wechatName="wechatName",
                    registerTime= nowTime,
                    phoneNumber = 18888888888,
                    emailAddress = "mai@dalaomai.cn",
                    updateTime=nowTime)
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
        self.assertEqual(user.verifyPassword("admin"),1)
        self.assertEqual(user.verifyPassword("****"),0)
        user.alterPassword("****")
        self.assertEqual(user.verifyPassword("****"),1)

        rules = user.getRules()
        self.assertEqual(len(rules),0)

        user.addRule(rule)
        rules = user.getRules()
        self.assertEqual(rules[0],rule)

        user.removeRule(rule)
        rules = user.getRules()
        self.assertEqual(len(rules),0)

        user.addRule(rule)
        user.removeRuleById(1)  ##
        rules = user.getRules()
        self.assertEqual(len(rules),0)
        pass
