#Message.py
import datetime

class Message():
    def __init__(self,title,href,time,id=None):
        self.id = id
        self.title = title
        self.time = time
        self.href = href
        self.updateTime = datetime.datetime.now()
        pass
