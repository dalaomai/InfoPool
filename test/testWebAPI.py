import unittest
from bin import API
from multiprocessing import Process
import requests
from config import API_HOST
import json
def apiRun():
    api = API()
    api.run()

class TestWebAPI(unittest.TestCase):

    def __init__(self, methodName = 'runTest'):
        self.apiP = Process(target=apiRun)
        self.apiP.start()
        return super().__init__(methodName)

    def testBaseMethod(self):
        result = requests.get('http://'+API_HOST+'/HtmlDownloadAPI')
        
        result = json.loads(result.text)
        self.assertEqual(result['url'],'')
        self.assertEqual(result['html'],-1)
        result = requests.get('http://'+API_HOST+'/HtmlDownloadAPI?url=http://www.foshan.gov.cn/zwgk/zwdt/jryw/')
        result = json.loads(result.text)
        self.assertEqual(result['url'],'http://www.foshan.gov.cn/zwgk/zwdt/jryw/')
        self.assertNotEqual(result['html'],-1)

        result = requests.post('http://'+API_HOST+'/HtmlParserAPI',data={})
        result = json.loads(result.text)
        self.assertEqual(result['matchs'],[''])
        self.assertEqual(result['messages'],[['','','']])
        data = {
                "webUrl":"http://www.foshan.gov.cn/zwgk/zwdt/jryw/",
                "rulePattern":'<li [\s\S]*?([0-9]{4}-[0-9]{2}-[0-9]{2})[\s\S]*?href="([\s\S]*?)"[\s\S]*?title="([\s\S]*?)" >',
                "ruleModel":"regular",
                "titlePosition":"2",
                "timePosition":"0",
                "hrefPosition":"1"
                }
        result = requests.post('http://'+API_HOST+'/HtmlParserAPI',data=json.dumps(data))
        result = json.loads(result.text)
        self.assertNotEqual(result['matchs'],[''])
        self.assertNotEqual(result['messages'],[['','','']])
        pass