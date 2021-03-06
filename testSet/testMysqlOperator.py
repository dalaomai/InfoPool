import unittest
from db.MysqlOperator import MysqlOperator
from common import Message,Rule,User
from config import DB_CONFIG
from datetime import datetime

class TestMysqlOperator(unittest.TestCase):
    user = User(id =1,
                userName='dalaomai',
                password='admin',
                wechatId='MAIZHILING',
                wechatName='dalaomai')
    rule = Rule(    id=1,
                    webName="佛山市人民政府",
                    webUrl = "http://www.foshan.gov.cn/zwgk/zwdt/jryw/",
                    ruleModel = "regular",
                    rulePattern=r'<li [\s\S]*?([0-9]{4}-[0-9]{2}-[0-9]{2})[\s\S]*?href="([\s\S]*?)"[\s\S]*?title="([\s\S]*?)" >',
                    titlePosition="2",
                    hrefPosition = "1",
                    timePosition="0",
                    isEffect = 1
                    )
    msg = Message("title","http://www.foshan.gov.cn/zwgk/zwdt/jryw/","2019-1-8")

    def testBaseProperty(self):
        mysqlOperator = MysqlOperator(DB_CONFIG)
        self.assertNotEqual(mysqlOperator.db,None)

    def testBaseMethod(self):
        mysqlOperator = MysqlOperator(DB_CONFIG)
        nowTime = datetime.now()


        msg = Message("title","href",nowTime.strftime("%Y-%m-%d"))
        self.rule.addMessage(msg)
        self.assertNotEqual(mysqlOperator.saveRules([self.rule]),-1)
        self.assertNotEqual(mysqlOperator.saveMessagesFromRule(self.rule),-1)
        self.assertNotEqual(mysqlOperator.saveUser(self.user),-1)
        self.assertNotEqual(len(mysqlOperator.getAllRules()),0)

        self.assertNotEqual(mysqlOperator.updateUserLastPushTimeForRule(self.user,self.rule,0),-1)
        self.assertNotEqual(len(mysqlOperator.getUnPushedUsers()),0)
        self.assertNotEqual(mysqlOperator.updateUserLastPushTimeForRule(self.user,self.rule,datetime.now()),-1)
        self.assertEqual(len(mysqlOperator.getUnPushedUsers()),0)

        return



