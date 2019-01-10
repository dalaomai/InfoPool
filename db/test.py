import unittest
from db.DataBase import DataBase
import config

class TestDb(unittest.TestCase):
    rule = {
    'webName':'test',
    'webUrl': 'http://test/',
    'ruleModel': 'regular',
    'rulePattern': r"<li class=[\s\S]*?href='([\s\S]*?)' title='([\s\S]*?)'[\s\S]*?([0-9]{4}-[0-9]{2}-[0-9]{2})",
    'titlePosition':'1',
    'timePosition':'2',
    'hrefPosition':'0'
    }
    info = {'title':'test','href':'test','time':'test','ruleId':'10'}

    def test_DataBase(self):
        data_base = DataBase(config.DB_CONFIG)
        self.assertIsNotNone(data_base.db,"test_DataBase::数据库初始失败！")
        self.assertNotEqual(data_base.storeRule(self.rule),-1,"test_DataBase::保存规则失败")
        rules = data_base.getRule()
        self.assertNotEqual(rules,-1,"test_DataBase::读取规则失败")
        if rules != -1:
            self.info['ruleId'] = rules[0]['id']
        self.assertNotEqual(data_base.storeInfo(self.info),-1,"test_DataBase::保存信息失败")
