#MysqlOperator.py
from db.DBOInterface import DBOInterface
from common import Message,Rule,User
from datetime import datetime
import pymysql
from util import logger

import pymysql

class MysqlOperator(DBOInterface):
    '''
    每次查询，务必重连、更新数据：self.db.begin()
    '''

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
        result = self.__saveValuesToDB(sql,values)
        return result

    def saveUser(self,user):
        assert type(user) == User,"类型错误"
        sql = "insert into User(userName,password,permission,wechatId,wechatName,registerTime,phoneNumber,emailAddress) values(%s,%s,%s,%s,%s,%s,%s,%s)"
        value= [user.userName,user.getPassword(),user.permission,user.wechatId,user.wechatName,user.registerTime,user.phoneNumber,user.emailAddress]
        cursor = self.db.cursor()
        try:
            result = cursor.execute(sql,value)
            self.db.commit()
            cursor.close()
            return result
        except Exception as e:
            self.db.rollback()
            cursor.close()
            if e.args[0]==1062:
                logger.warning(e.args[1])
                return 0
            logger.error("Failed:" + str(sql),exc_info=True)
            return -1
        pass
        return result

    def getAllRules(self):
        '''
        return id,webName,webUrl,ruleModel,rulePattern,titlePosition,timePosition,hrefPosition,isEffect,updateTime
        '''

        sql = "select id,webName,webUrl,ruleModel,rulePattern,titlePosition,hrefPosition,timePosition,isEffect,updateTime from Rule "
        executeResults = self.__getFromDB(sql)
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

    def getUnPushedUsers(self):
        '''
        '''
        sql = "select distinct userId, wechatId from UnPushed"
        results = self.__getFromDB(sql)
        users = []
        for result in results:
            user = User(id=result[0],wechatId=result[1])
            self.__getUnPushedRulesSaveInUser(user)
            users.append(user)
        return users

    def updateUserLastPushTimeForRule(self,user,rule,time=datetime.now()):
        '''
        '''
        sql = "update User_Rule set lastPushTime = %s where userId = %s and ruleId = %s"
        value = [time,user.id,rule.id]
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

    def __getUnPushedRulesSaveInUser(self,user):
        '''
        '''
        sql = "select distinct ruleId,webName,webUrl,lastPushTime from UnPushed where userId = " + str(user.id)
        results = self.__getFromDB(sql)
        for result in results:
            rule = Rule(id=result[0],webName=result[1],webUrl=result[2],subscribeLastPushTime=result[3])
            self.__getUnPushedMessagesSaveInRule(rule)
            user.addRule(rule)
        return 0

    def __getUnPushedMessagesSaveInRule(self,rule):
        '''
        '''
        sql = "select title,href,time from UnPushed where ruleId = " + str(rule.id)
        results = self.__getFromDB(sql)
        for result in results:
            rule.addMessage(Message(title=result[0],href=result[1],time=result[2]))
        return 0

    def __saveValueToDB(self,sql,value):
        cursor = self.db.cursor()
        try:
            result = cursor.execute(sql,value)
            self.db.commit()
            cursor.close()
            return result
        except Exception as e:
            self.db.rollback()
            cursor.close()
            logger.error("Failed:" + str(sql),exc_info=True)
            return -1
        pass

    def __saveValuesToDB(self,sql,values):
        cursor = self.db.cursor()
        try:
            result = cursor.executemany(sql,values)
            self.db.commit()
            cursor.close()
            return result
        except Exception as e:
            self.db.rollback()
            cursor.close()
            logger.error("Failed:" + str(sql),exc_info=True)
            return -1
        pass

    def __getFromDB(self,sql,value=[]):
        self.db.begin()
        cursor = self.db.cursor()
        try:
            results = cursor.execute(sql,value)
            if results == 0:
                return []
            results = cursor.fetchall()
            cursor.close()
            return results
        except Exception as e:
            cursor.close()
            logger.error("Failed :" + str(sql),exc_info=True)
            return []