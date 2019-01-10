
import unittest
from test import TestMessage,TestRule,TestUser,TestHtmlDownload,TestHtmlParser,TestMysqlOperator,TestWechatPush


if __name__ == '__main__':
    suite = unittest.TestSuite()

    suite.addTest(TestMessage("testBaseProperty"))
    suite.addTest(TestRule("testBaseProperty"))
    suite.addTest(TestRule("testBaseMethod"))
    suite.addTest(TestUser("testBaseProperty"))
    suite.addTest(TestHtmlDownload("testBaseProperty"))
    suite.addTest(TestHtmlParser("testParser"))
    suite.addTest(TestMysqlOperator("testBaseMethod"))
    suite.addTest(TestWechatPush("testBaseMethod"))


    runner = unittest.TextTestRunner()
    runner.run(suite)
