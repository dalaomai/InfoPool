#testHtmlDownload.py
import unittest
from common.HtmlDownload import HtmlDownload

class TestHtmlDownload(unittest.TestCase):
    def testBaseProperty(self):
        r = HtmlDownload.download('https://www.baidu.com/')
        self.assertIsNotNone(r)

