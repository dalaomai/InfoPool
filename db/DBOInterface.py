#DBOInterface.py
from abc import ABCMeta,abstractmethod

class DBOInterface():
    __metaclass__ = ABCMeta

    @abstractmethod
    def __init__(self,db_config):
        pass

    @abstractmethod
    def saveMessagesFromRule(self,rule):
        pass

    @abstractmethod
    def getAllRules(self):
        pass

    @abstractmethod
    def saveUser(self,user):
        pass

    @abstractmethod
    def saveRule(self,rules):
        pass

    @abstractmethod
    def getUnpushedUsers(self):
        pass

    @abstractmethod
    def updateUserLastPushTimeForRule(self,user,rule):
        pass