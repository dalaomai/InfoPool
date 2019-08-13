# start.py

from bin import InfoCrawl, WechatPush
from config import START_SLEEP_TIME
from util import logger
from time import sleep
# from multiprocessing import Process
import threading
from bin import API
from common.ToolSet import countDown

ic = InfoCrawl()
wp = WechatPush()


def apiRun():
    api = API()
    api.run()


def spiderAndPusherRun():
    while(1):
        logger.info("####start the spider####")
        ic.run()
        logger.info("####start the wechatPush####")
        wp.push()
        logger.info("####sleep " + str(START_SLEEP_TIME) + " seconds####")
        countDown(START_SLEEP_TIME)


if __name__ == '__main__':
    # apiProcess = Process(target=apiRun)
    # spProcess = Process(target=spiderAndPusherRun)
    # #apiProcess.start()
    # spProcess.start()
    # #apiProcess.join()
    # spProcess.join()
    apiThread = threading.Thread(target=apiRun)
    apiThread.start()
    spThread = threading.Thread(target=spiderAndPusherRun)
    spThread.start()
    


