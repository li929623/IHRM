import os
import logging
from logging import handlers
import time
#绝对路径
BASE_DIR= os.path.dirname(os.path.abspath(__file__))

BASE_URL= "http://ihrm-test.itheima.net"

TOKEN=None
headers_data={"Content-Type":"application/json",
              "Authorization":"Bearer ***"}

def init_log_config():
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    # 创建控制台处理器
    sh = logging.StreamHandler()
    # 创建文件处理器
    log_path = BASE_DIR + "/log/text.log"
    fh = logging.handlers.TimedRotatingFileHandler(log_path, when="MIDNIGHT", interval=5, backupCount=7)

    # fmt设置格式化
    fmt ="[%(asctime)s] [%(levelname)8s] --- %(message)s (%(filename)s:%(lineno)s)"
    formatter = logging.Formatter(fmt)

    # 设置到日志中
    sh.setFormatter(formatter)
    fh.setFormatter(formatter)

    logger.addHandler(sh)
    logger.addHandler(fh)



