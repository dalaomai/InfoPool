from common import *
import web
from util import *
import json
class HtmlParserAPI(object):
    def __init__(self, *args, **kwargs):
        self.__result = {
            'matchs':[''],
            'messages':[('','','')]
            }
        self.__parser = HtmlParser()

    def POST(self):
        inputs= web.data().decode('utf-8')
        try:
            inputs = json.loads(inputs)
            rule = Rule(webUrl=inputs['webUrl'],
                        rulePattern=inputs['rulePattern'],
                        ruleModel=inputs['ruleModel'],
                        titlePosition=inputs['titlePosition'],
                        timePosition=inputs['timePosition'],
                        hrefPosition=inputs['hrefPosition'])
            html = HtmlDownload.download(rule.webUrl)
            messages,matchs = self.__parser.parseForAPI(html,rule)
        except Exception as e:
            logger.warning('',exc_info=True)
            return json.dumps(self.__result)
        self.__result['matchs'] = matchs
        msgs=[]
        for msg in messages:
            msgs.append([msg.title,msg.href,msg.time])
        self.__result['messages'] = msgs
        return json.dumps(self.__result)
    
    def GET(self):
        return json.dumps(self.__result)