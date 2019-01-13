#start.py

from bin import InfoCrawl,WechatPush
from config import START_SLEEP_TIME,DB_CONFIG,_DB_CONFIG
from util import logger
from time import sleep
import argparse

ic =InfoCrawl()
wp = WechatPush()

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-db',help='select database configuration')
    args = parser.parse_args()
    if args.db != None:
        DB_CONFIG = _DB_CONFIG[args.db]

    while(1):
        logger.info("####start the spider####")
        ic.run()
        logger.info("####start the wechatPush####")
        wp.push()
        logger.info("####sleep " + str(START_SLEEP_TIME) + " seconds####")
        sleep(START_SLEEP_TIME)