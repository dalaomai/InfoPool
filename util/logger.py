#logger.py
import logging
import os.path
from datetime import datetime

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter("%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s")

nowTimeStr = datetime.now().strftime('%Y%m%d%H%M')
log_path = os.getcwd() + '/Logs'
log_name = log_path + '/' + nowTimeStr + '.log'
if not os.path.exists(log_path):
    os.makedirs(log_path)

fileHandler = logging.FileHandler(log_name,mode='a')
fileHandler.setLevel(logging.DEBUG)

consoleHandler = logging.StreamHandler()
consoleHandler.setLevel(logging.INFO)

fileHandler.setFormatter(formatter)
consoleHandler.setFormatter(formatter)

logger.addHandler(fileHandler)
logger.addHandler(consoleHandler)


