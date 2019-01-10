#start.py

from bin import InfoCrawl,WechatPush
from config import START_SLEEP_TIME
from util import logger
from time import sleep

ic =InfoCrawl()
wp = WechatPush()

if __name__ == '__main__':
    while(1):
        logger.info("####start the spider####")
        ic.run()
        logger.info("####start the wechatPush####")
        wp.push()
        logger.info("####sleep " + str(START_SLEEP_TIME) + " seconds####")
        sleep(START_SLEEP_TIME)