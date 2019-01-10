import pymysql
from util.logger import logger



class MysqlHelper():

    def __init__(self,db_config):

        #连接数据库
        try:
            self.db = pymysql.connect(host=db_config['host'],
                                    port=db_config['port'],
                                    user =db_config['user'],
                                    password=db_config['password'],
                                    db = db_config['db'])
        except Exception as e:
            logger.error("Failed to connect MysqlDB",exc_info=True)
        return

    def insert_db_rule(self,rule):
        '''
        插入单条规则到数据库

        rules::dict
        '''

        #生成sql语句
        if 'updateTime' not in rule.keys():
            sql = "insert into rule(webName,webUrl,rulePattern,ruleModel,titlePosition,timePosition,hrefPosition) values(%s,%s,%s,%s,%s,%s,%s)"
        else:
            sql = "insert into rule(webName,webUrl,rulePattern,ruleModel,titlePosition,timePosition,hrefPosition,updateTime) values(%s,%s,%s,%s,%s,%s,%s,%s)"

        #生成值
        try:
            values=[rule['webName'],rule['webUrl'],rule['rulePattern'],rule['ruleModel'],rule['titlePosition'],rule['timePosition'],rule['hrefPosition']]
            if 'updateTime' in rule.keys():
                values.append(rule['updateTime'])
        except Exception as e:
            processException('10002',2)
            return -1

        #发起数据插入
        cursor = self.db.cursor()
        try:
            result = cursor.execute(sql,values)
            self.db.commit()
            cursor.close()
        except Exception as e:
            self.db.rollback()  #插入失败回滚数据库
            processException('10003',e)
            cursor.close()
            return -1
        return result

    def select_db_rule(self,isEffect=True):
        #生成sql语句
        sql = "select id,webName,webUrl,ruleModel,rulePattern,titlePosition,timePosition,hrefPosition,isEffect from rule where isEffect=%s"

        cursor = self.db.cursor()
        results = []
        try:
            cursor.execute(sql,[isEffect])
            result = cursor.fetchall()
            cursor.close()
        except Exception as e:
            cursor.close()
            processException('10005',e)
            return -1
        for r in result:
            results.append({'id':r[0],
                            'webName':r[1],
                            'webUrl':r[2],
                            'ruleModel':r[3],
                            'rulePattern':r[4],
                            'titlePosition':r[5],
                            'timePosition':r[6],
                            'hrefPosition':r[7],
                            'isEffect':r[8]})
        return results

    def insert_db_info(self,infos=[{}]):
        '''
        插入多条信息数据到数据库中

        infos::list::dict
        或
        infos::dict
        '''

        #假如传入的是只有一条信息的字典
        if type(infos).__name__ == 'dict':
            infos=[infos]

        #生成插入sql语句
        sql = "insert into information(title,href,time,ruleId) select %s,%s,%s,%s \
                from dual where not exists(select title from information where title=%s and ruleId=%s)"
        #生成值
        try:
            values=[]
            for info in infos:
                value = [str(info['title']),str(info['href']),str(info['time']),int(info['ruleId']),str(info['title']),int(info['ruleId'])]
                values.append(value)
        except Exception as e:
            processException('10006',e)
            return -1

        #插入数据到数据库
        cursor = self.db.cursor()
        try:
            result = cursor.executemany(sql,values)
            self.db.commit()
            cursor.close()
        except Exception as e:
            self.db.rollback()
            cursor.close()
            processException('10007',e)
            return -1
        return result

    def select_db_info(self,limitValues=1):

        sql = "select * from info limit %s"
        cursor = self.db.cursor()

        try:
            cursor.execute(sql,[limitValues])
            result = cursor.fetchall()
            cursor.close()
        except Exception as e:
            cursor.close()
            processException('10008',e)
            return -1
        return result

   


if __name__=='__main__':
    import sys
    sys.path.append(r'C:\Users\dalaomai\Source\Accurate_recommendation\ProjectSourceCode\InFoPool')
    from config import DB_CONFIG
    rule = {
    'webName':'佛山市人民政府门户网站',
    'webUrl': 'http://www.foshan.gov.cn/',
    'ruleModel': 'regular',
    'rulePattern': r"<li class=[\s\S]*?href='([\s\S]*?)' title='([\s\S]*?)'[\s\S]*?([0-9]{4}-[0-9]{2}-[0-9]{2})",
    'titlePosition':'1',
    'timePosition':'2',
    'hrefPosition':'0'
    }
    rule = {
    'webName':'纽约时报中文网-手机',
    'webUrl': 'https://m.cn.nytimes.com/',
    'ruleModel': 'regular',
    'rulePattern': r'<li class="regular-item"><a href="([\s\S]*?)" title="([\s\S]*?)">[\s\S]*?</li>',
    'titlePosition':'1',
    'timePosition':'0',
    'hrefPosition':'-1'
    }
    
    info = {'title':'test','href':'test','time':'test','ruleId':'10'}

    mysql = MysqlHelper(DB_CONFIG)
    #mysql.insert_db_info(info)
    mysql.insert_db_rule(rule)
    print(mysql.select_db_rule())