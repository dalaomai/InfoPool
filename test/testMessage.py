#testMessage.py
import unittest
import datetime
from common.Message import Message


class TestMessage(unittest.TestCase):

    def testBaseProperty(self):
        nowTime = datetime.datetime.now()
        msg = Message("title","href",nowTime)
        self.assertEqual(msg.title,"title")
        self.assertEqual(msg.href,"href")
        self.assertEqual(msg.time,nowTime)
        self.assertEqual(msg.id,None)
        self.assertEqual(type(msg.updateTime),type(nowTime))

        msg = Message("title","href",nowTime,1)
        self.assertEqual(msg.id,1)
        pass



