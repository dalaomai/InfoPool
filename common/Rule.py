#Rule.py
from datetime import datetime
from common import Message


class Rule():

    def __init__(self, *args, **kwargs):
        '''
        //规则属性
        id:int
        webName:string
        webUrl:string
        updateTime:date
        rulePattern:string
        ruleModel:string
        titlePosition:string
        timePosition:string
        hrefPosition:string
        isEffect:boolean
        //订阅相关
        subscribeIsPush:boolean
        subscribeLastPushTime:date
        subscribeAddTime:date
        //
        messages[]:Message		所拥有的消息
        '''
        self.id = None
        self.webName = None
        self.webUrl = None
        self.rulePattern = None
        self.ruleModel = None
        self.titlePosition = None
        self.hrefPosition = None
        self.timePosition = None
        self.isEffect = None
        self.updateTime = datetime.now()

        self.subscribeIsPush = None
        self.subscribeLastPushTime = None
        self.subscribeUpdateTime = datetime.now()

        self.__messages = []

        self.alterRule(**kwargs)
        return
    
    def alterRule(self,**kwargs):
        '''
        修改规则的基本属性，不包括所包含的“消息”
        '''
        self.id = kwargs.get("id",self.id)
        self.webName = kwargs.get("webName",self.webName)
        self.webUrl = kwargs.get("webUrl",self.webUrl)
        self.rulePattern = kwargs.get("rulePattern",self.rulePattern)
        self.ruleModel = kwargs.get("ruleModel",self.ruleModel)
        self.titlePosition = kwargs.get("titlePosition",self.titlePosition)
        self.hrefPosition = kwargs.get("hrefPosition",self.hrefPosition)
        self.timePosition = kwargs.get("timePosition",self.timePosition)
        self.isEffect = kwargs.get("isEffect",self.isEffect)
        self.updateTime = kwargs.get("updateTime",self.updateTime)

        self.subscribeIsPush = kwargs.get("subscribeIsPush",self.subscribeIsPush)
        self.subscribeLastPushTime = kwargs.get("subscribeLastPushTime",self.subscribeLastPushTime)
        self.subscribeUpdateTime = kwargs.get("subscribeUpdateTime",self.subscribeUpdateTime)

        return

    def getMessages(self):
        '''
        返回规则所拥有的消息
        '''
        return self.__messages

    def addMessage(self,newMsg):
        assert type(newMsg)==Message.Message,"类型出错"
        self.__messages.append(newMsg)
        return

    def removeMessage(self,msg):
        assert type(msg)==Message.Message,"类型出错"
        self.__messages.remove(msg)
        return

    def removeMessageById(self,MsgId):
        '''
        移除指定消息
        '''
        for msg in self.__messages:
            if msg.id == MsgId:
                self.removeMessage(msg)
                return
        return



