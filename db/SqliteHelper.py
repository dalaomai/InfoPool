# coding:utf-8
import datetime
from urllib import parse
from sqlalchemy import Column, Integer, String, DateTime, Numeric, create_engine, VARCHAR
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from config import DB_CONFIG



BaseModel = declarative_base()


class Info(BaseModel):
    __tablename__ = 'INFO'
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String,nullable=False)
    href = Column(String,nullable=False)
    time = Column(String,nullable=False)
    url = Column(String,nullable=False)
    webname = Column(String,nullable=False)
    updatetime = Column(DateTime(), default=datetime.datetime.utcnow)



class SqlHelper():
    params = {'title':Info.title,'href':Info.href,'time':Info.time,'webname':Info.webname,'updatetime':Info.updatetime}

    def __init__(self,db_config):
        print(db_config['DB_CONNECT_STRING'])
        if 'sqlite' in db_config['DB_CONNECT_STRING']:
            connect_args = {'check_same_thread': False}
            self.engine = create_engine(db_config['DB_CONNECT_STRING'], echo=False, connect_args=connect_args)
        else:
            self.engine = create_engine(db_config['DB_CONNECT_STRING'], echo=False)
        DB_Session = sessionmaker(bind=self.engine)
        self.session = DB_Session()

    def init_db(self):
        BaseModel.metadata.create_all(self.engine)
        return

    def drop_db(self):
        BaseModel.metadata.drop_all(self.engine)
        return

    def insert(self, value):
        info = Info(title=value['title'], href=value['href'], time=value['time'], url=value['url'],webname=value['webname'])
        #同一网站的同一内容不再插入
        query = self.session.query(Info.title,Info.webname)
        query = query.filter(Info.title==value['title'],Info.webname==value['webname'])
        if len(query.all())>0:
            return
        self.session.add(info)
        self.session.commit()
        return

    def select(self, conditions=""):
        '''
        conditions::string sql语句不包括select...from...
        '''
        sqlStr = "select title,href,time,url,webname from " + Info.__tablename__ + '\n' + conditions
        print(sqlStr)
        selece_result = self.session.execute(sqlStr)
        result = []
        for i in selece_result.fetchall():
            temp = {}
            temp['title'] = i[0]
            temp['href'] = parse.urljoin(i[3],i[1])
            temp['time'] = i[2]
            temp['url'] = i[3]
            temp['webname'] = i[4]
            result.append(temp)
        return result

    def close(self):
        self.session.close()
        return




