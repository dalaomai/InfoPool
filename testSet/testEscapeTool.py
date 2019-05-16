import unittest
from common.EscapeTool import EscapeTool

class TestEscapeTool(unittest.TestCase):

    def testBaseMethod(self):
        self.assertEqual(EscapeTool.replace(r'sadf\d\d\dasdf\d\dasd\sadff\d',r'\d',r'代替'),r'sadf\d代替asdf\dasd\sadff代替')
        self.assertEqual(EscapeTool.insert(r'asdf\dasd',r'\d'),r'asdf\d\dasd')