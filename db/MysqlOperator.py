#MysqlOperator.py
from db.DBOInterface import DBOInterface
from common import Message,Rule,User
from datetime import datetime
import pymysql
from util import logger

import pymysql

class MysqlOperator(DBOInterface):

    def __init__(self, db_config):
        #连接数据库
        try:
            self.db = pymysql.connect(host=db_config['host'],
                                    port=db_config['port'],
                                    user =db_config['user'],
                                    password=db_config['password'],
                                    db = db_config['db'])
        except Exception as e:
            logger.error("Failed to connect MysqlDB",exc_info=True)
        return

    def saveMessagesFromRule(self, rule):

        sql = "insert into Message(title,href,time,ruleId) select %s,%s,%s,%s \
                from dual where not exists(select title from Message where title=%s and ruleId=%s)"
        values=[]
        messages = rule.getMessages()
        for msg in messages:
            values.append([msg.title,msg.href,msg.time,rule.id,msg.title,rule.id])

        cursor = self.db.cursor()
        try:
            result = cursor.executemany(sql,values)
            self.db.commit()
            cursor.close()
        except Exception as e:
            self.db.rollback()
            cursor.close()
            logger.error("Failed to saveMessagesFromRules",exc_info=True)
            return -1
        return result

    def getAllRules(self):
        '''
        return id,webName,webUrl,ruleModel,rulePattern,titlePosition,timePosition,hrefPosition,isEffect,updateTime
        '''

        sql = "select id,webName,webUrl,ruleModel,rulePattern,titlePosition,hrefPosition,timePosition,isEffect,updateTime from Rule "
        cursor = self.db.cursor()
        try:
            cursor.execute(sql)
            executeResults = cursor.fetchall()
            cursor.close()
        except Exception as e:
            cursor.close()
            logger.error("Failed to getAllRules",exc_info=True)
            return -1
        rules=[]
        for executeResult in executeResults:
            rule = Rule(id = executeResult[0],
                        webName=executeResult[1],
                        webUrl =executeResult[2],
                        ruleModel = executeResult[3],
                        rulePattern=executeResult[4],
                        titlePosition=executeResult[5],
                        hrefPosition = executeResult[6],
                        timePosition=executeResult[7],
                        isEffect = executeResult[8],
                        updateTime=executeResult[9])
            rules.append(rule)
        return rules

    def saveUser(self,user):
        assert type(user) == User,"类型错误"
        sql = "insert into User(userName,password,permission,wechatId,wechatName,registerTime,phoneNumber,emailAddress) values(%s,%s,%s,%s,%s,%s,%s,%s)"
        values= [user.userName,user.getPassword(),user.permission,user.wechatId,user.wechatName,user.registerTime,user.phoneNumber,user.emailAddress]
        cursor = self.db.cursor()
        try:
            result = cursor.execute(sql,values)
            self.db.commit()
            cursor.close()
        except Exception as e:
            self.db.rollback()
            cursor.close()
            if e.args[0] == 1062:
                logger.warning(e.args[1])
                return -2
            logger.error("Failed to saveUser",exc_info=True)
            return -1
        return result

    def saveRules(self,rules):
        '''
        '''
        sql = "insert into Rule(webName,webUrl,rulePattern,ruleModel,titlePosition,timePosition,hrefPosition,isEffect,updateTime)\
       select %s,%s,%s,%s,%s,%s,%s,%s,%s from dual\
      where not exists(select webName from Rule where webUrl = %s and rulePattern = %s)"

        values = []
        rule = Rule()
        for rule in rules:
            values.append([rule.webName,
                           rule.webUrl,
                           rule.rulePattern,
                           rule.ruleModel,
                           rule.titlePosition,
                           rule.timePosition,
                           rule.hrefPosition,
                           rule.isEffect,
                           rule.updateTime,
                           rule.webUrl,
                           rule.rulePattern])
        cursor = self.db.cursor()
        try:
            result = cursor.executemany(sql,values)
            self.db.commit()
            cursor.close()
        except Exception as e:
            self.db.rollback()
            cursor.close()
            logger.error("Failed to save rules",exc_info=True)
            return -1
        return result

    def getUnpushedUsers(self):
        '''
        '''
        sql = "select distinct userId, wechatId from Unpushed"
        cursor = self.db.cursor()
        try:
            results = cursor.execute(sql)
            results = cursor.fetchall()
            cursor.close()
        except Exception as e:
            cursor.close()
            logger.error("Failed to getUnpushedUsers",exc_info=True)
            return []
        users = []
        for result in results:
            user = User(id=result[0],wechatId=result[1])
            self.getUnpushedRulesSaveInUser(user)
            users.append(user)
        return users

    def getUnpushedRulesSaveInUser(self,user):
        '''
        '''
        sql = "select distinct ruleId,webName,webUrl,lastPushTime from Unpushed where userId = " + str(user.id)
        cursor = self.db.cursor()
        try:
            results = cursor.execute(sql)
            results = cursor.fetchall()
            cursor.close()
        except Exception as e:
            cursor.close()
            logger.error("Failed to getUnpushedRulesSaveInUser",exc_info=True)
            return -1
        for result in results:
            rule = Rule(id=result[0],webName=result[1],webUrl=result[2],subscribeLastPushTime=result[3])
            self.getUnpushedMessagesSaveInRule(rule)
            user.addRule(rule)
        return 0

    def getUnpushedMessagesSaveInRule(self,rule):
        '''
        '''
        sql = "select title,href,time from Unpushed where ruleId = " + str(rule.id)
        cursor = self.db.cursor()
        try:
            results = cursor.execute(sql)
            results = cursor.fetchall()
            cursor.close()
        except Exception as e:
            cursor.close()
            logger.error("Failed to getUnpushedMessagesSaveInRule",exc_info=True)
            return -1
        for result in results:
            rule.addMessage(Message(title=result[0],href=result[1],time=result[2]))
        return 0

    def updateUserLastPushTimeForRule(self,user,rule):
        '''
        '''
        sql = "update User_Rule set lastPushTime = %s where userId = %s and ruleId = %s"
        value = [datetime.now(),user.id,rule.id]
        cursor = self.db.cursor()
        try:
            result = cursor.execute(sql,value)
            self.db.commit()
            cursor.close()
        except Exception as e:
            self.db.rollback()
            cursor.close()
            logger.error("Failed to updateUserLastPushTime",exc_info=True)
            return -1
        return result

