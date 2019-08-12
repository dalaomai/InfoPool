from common import *
import web
from util import *
import json
from datetime import datetime
class HtmlParserAPI(object):
    def __init__(self, *args, **kwargs):
        self.__result = {
            'matchs':[''],
            'messages':[('','','')]
            }
        self.htmlDownload = HtmlDownload()
        self.__parser = HtmlParser()

    def POST(self):
        inputs= web.data().decode('utf-8')
        logger.debug(inputs)
        
        try:
            inputs = json.loads(inputs)
        except Exception as e:
            logger.warning('the date is not right: ' + str(inputs))
            return json.dumps(self.__result)
        
        try:
            rule = Rule(webUrl=inputs['webUrl'],
                        webModel=inputs['webModel'],
                        rulePattern=inputs['rulePattern'],
                        ruleModel=inputs['ruleModel'],
                        titlePosition=inputs['titlePosition'],
                        timePosition=inputs['timePosition'],
                        hrefPosition=inputs['hrefPosition'])
            date = inputs.get('date','2019-01-01')
            html = self.htmlDownload.download(rule.webUrl,rule.webModel,date=datetime.strptime(date,r'%Y-%m-%d'))
            messages,matchs = self.__parser.parseForAPI(html,rule)
        except Exception as e:
            logger.error('',exc_info=True)
            return json.dumps(self.__result)
    
        self.__result['matchs'] = matchs
        msgs=[]
        for msg in messages:
            msgs.append([msg.title,msg.href,msg.time])
        self.__result['messages'] = msgs
        return json.dumps(self.__result)
    
    def GET(self):
        return json.dumps(self.__result)