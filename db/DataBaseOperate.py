from db.DBOInterface import DBOInterface
from config import DB_CONFIG
from util import logger
from datetime import datetime


class DataBaseOperate(DBOInterface):
    '''
    数据库操作集合

    '''
    
    def __init__(self,db_config=DB_CONFIG):
        self.__operator = None

        try:
            if db_config['type'] == 'mysql':
                from db.MysqlOperator import MysqlOperator
                self.__operator = MysqlOperator(db_config)
            else:
                raise Exception('数据库选择失败！')
        except Exception as e:
            logger.error("数据库选择失败",exc_info=True)
        return

    def saveMessagesFromRule(self,rule):
        return self.__operator.saveMessagesFromRule(rule)

    def getAllRules(self):
        return self.__operator.getAllRules()

    def saveUser(self,user):
        return self.__operator.saveUser(user)

    def saveRule(self, rules):
        return self.__operator.saveRule(rules)

    def getUnPushedUsers(self):
        return self.__operator.getUnPushedUsers()

    def updateUserLastPushTimeForRule(self,user,rule,time=datetime.now()):
        return self.__operator.updateUserLastPushTimeForRule(user,rule,time)






