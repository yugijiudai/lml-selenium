# Author : lml
# Date : 2021/12/6
# -*- coding:utf-8 -*-

"""
文件说明
"""
import sys

from loguru import logger

from src.main.code.util.ResourceUtil import ResourceUtil


def init_log():
    file = f'{ResourceUtil.get_root_path()}/logs/selenium.log'
    logger.add(file, format="{time:YYYY-MM-DD at HH:mm:ss} | {level} | {message}", level="INFO")
    # 文件过大就会重新生成一个文件
    logger.add(file, rotation="100 MB", enqueue=True, serialize=True)
    # 保存zip格式
    # logger.add(file, compression="zip")
    logger.info("日志初始化成功...")


# 初始化日志相关配置
init_log()


class MyLogger:
    """
    日志配置
    """

    # 异常信息打印
    @staticmethod
    def log_error(msg=None):
        exc_type, exc_value, exc_traceback = sys.exc_info()
        traceback_details = {
            "filename": exc_traceback.tb_frame.f_code.co_filename,
            "lineno": exc_traceback.tb_lineno,
            "name": exc_traceback.tb_frame.f_code.co_name,
            "type": exc_type.__name__,
            "message": exc_value
        }
        logger.error("{}-{}", msg, traceback_details)
