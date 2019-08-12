
import unittest
import sys


from testSet import *


if __name__ == '__main__':
    suite = unittest.TestSuite()

    suite.addTest(TestMessage("testBaseProperty"))
    suite.addTest(TestRule("testBaseProperty"))
    suite.addTest(TestRule("testBaseMethod"))
    suite.addTest(TestUser("testBaseProperty"))
    suite.addTest(TestUser("testBaseMethod"))
    suite.addTest(TestHtmlDownload("testBaseProperty"))
    suite.addTest(TestHtmlParser("testParser"))
    suite.addTest(TestMysqlOperator("testBaseMethod"))
    suite.addTest(TestMysqlOperator("testBaseProperty"))
    suite.addTest(TestWechatPush("testBaseMethod"))
    suite.addTest(TestEscapeTool("testBaseMethod"))
    suite.addTest(TestWebAPI("testBaseMethod"))   


    runner = unittest.TextTestRunner()
    runner.run(suite)
