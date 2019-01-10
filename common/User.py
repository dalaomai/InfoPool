#User.py
from datetime import datetime
import hashlib
from common import Rule
from datetime import datetime

class User():

    def __init__(self, *args, **kwargs):
        self.id = None
        self.userName = None
        self.__password = None
        self.permission = None
        self.wechatId = None
        self.wechatName = None
        self.registerTime = None
        self.phoneNumber = None
        self.emailAddress = None
        self.updateTime = datetime.now()
        self.__rules = []

        self.alterUserInformation(**kwargs)

        return

    def alterUserInformation(self,**kwargs):
        self.id = kwargs.get("id",self.id)
        self.userName = kwargs.get("userName",self.userName)

        if kwargs.get("password",self.__password) != None:
            self.alterPassword(kwargs.get("password",self.__password))

        self.permission = kwargs.get("permission",self.permission)
        self.wechatId = kwargs.get("wechatId",self.wechatId)
        self.wechatName = kwargs.get("wechatName",self.wechatName)
        self.registerTime = kwargs.get("registerTime",self.registerTime)
        self.phoneNumber = kwargs.get("phoneNumber",self.phoneNumber)
        self.emailAddress = kwargs.get("emailAddress",self.emailAddress)
        self.updateTime = kwargs.get("updateTime",self.updateTime)
        return

    def alterPassword(self,password):
        '''
        修改密码，明文密码转换为md5
        '''
        md5 = hashlib.md5()
        md5.update(password.encode())
        self.__password = md5.hexdigest()
        return

    def verifyPassword(self,password):
        '''
        验证密码是否正确
        '''
        md5 = hashlib.md5()
        md5.update(password.encode())
        if self.__password == md5.hexdigest():
            return 1
        else:
            return 0

    def getPassword(self):
        '''
        '''
        return self.__password

    def addRule(self,rule):
        assert type(rule)==Rule.Rule,"类型错误"
        self.__rules.append(rule)
        return

    def getRules(self):
        '''
        '''
        return self.__rules

    def removeRule(self,rule):
        assert type(rule)==Rule.Rule,"类型错误"
        self.__rules.remove(rule)
        return

    def removeRuleById(self,ruleId):
        for rule in self.__rules:
            if rule.id == ruleId:
                self.removeRule(rule)
                return
        return




