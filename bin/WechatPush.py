#WechatPush.py
from util import logger
from db import DataBaseOperate
from common import User,Rule,Message
import requests
import json
import random
from datetime import datetime
from config import WECHAT_CONFIG

class WechatPush():
    def __init__(self, *args, **kwargs):
        self.__accessToken = None
        self.getAccessToken()
        self.__count = 0
        self.__DBOperator = DataBaseOperate()
        return

    def push(self):
        users = self.__DBOperator.getUnPushedUsers()
        logger.info("Get " + str(len(users)) + " users to push")
        for user in users:
            for rule in user.getRules():
                result = 0
                for message in rule.getMessages():
                    result = self.sendMessages(user,self.structureMessageTextByMessage(message))
                    if result == -1:
                        break
                if result != -1:
                    self.__DBOperator.updateUserLastPushTimeForRule(user,rule,datetime.now())
        return 0

    def sendMessages(self,user,text):
        '''
        '''
        url = "https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token=" + self.__accessToken
        data = {
                "touser" : user.wechatId,
                "msgtype" : "text",
                "agentid" : WECHAT_CONFIG['AgentId'],
                "text" : {
                            "content" : text
                            },
                "safe":0
                }
        try:
            result = requests.post(url,json.dumps(data))
            result = json.loads(result.text)
            if result['errcode'] != 0:
                self.getAccessToken()
                url = "https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token=" + self.__accessToken
                result = requests.post(url,json.dumps(data))
                result = json.loads(result.text)
        except Exception as e:
            logger.error("Post wechat push failed",exc_info=True)

        if result['errcode'] != 0 or result['invaliduser'] != '':
            logger.error("Post wechat push failed.\n result :" + json.dumps(result) + "\ndata: " + json.dumps(data))
            return -1

        return 0

    def structureMessageTextByRule(self,rule):
        assert type(rule)==Rule,类型错误
        resultText = ''
        resultText += '<a href="'+ rule.webUrl + self.count() + '">'+ rule.webName + '</a>' + '\n----------------\n'
        for msg in rule.getMessages():
            resultText += '·<a href="'+ msg.href + self.count() + '">'+ msg.title + '</a>\n'
        resultText += '\n\n'
        return resultText

    def structureMessageTextByMessage(self,message):
        assert type(message)==Message,类型错误
        return '<a href="'+ message.href + '">'+ message.title + '</a>\n'

    def count(self):
        '''
        向url后增加‘#*=count'，解决安卓客户端显示问题
        '''
        if self.__count > 100:
            self.__count = 0
        self.__count +=1 
        return "#*=" + str(self.__count)

    def getAccessToken(self):
        try:
            url = 'https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid='+ WECHAT_CONFIG['CorpId'] +'&corpsecret=' +  WECHAT_CONFIG['Secret']
            result = json.loads(requests.get(url).text)
        except Exception as e:
            logger.error("Get wechat accessToken failed",exc_info=True)
            return -1

        if result['errcode'] == 0:
            self.__accessToken = result['access_token']
            return 0
        else:
            logger.error("Get wechat accessToken failed :" + str(result))
        return -1

if __name__=="__main__":
    wp = WechatPush()
    wp.push()