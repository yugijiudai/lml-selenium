# Author : lml
# Date : 2021/12/6
# -*- coding:utf-8 -*-

"""
文件说明
"""
import sys

from loguru import logger


def init_log():
    file = '/Volumes/common/logs/selenium.log'
    logger.add(file, format="{time:YYYY-MM-DD at HH:mm:ss} | {level} | {message}", level="INFO")
    # 文件过大就会重新生成一个文件
    logger.add(file, rotation="500 MB")
    # 每天12点创建新文件
    logger.add(file, rotation="12:00")
    # 文件时间过长就会创建新文件
    logger.add(file, rotation="1 week")
    # 一段时间后会清空
    logger.add(file, retention="10 days")
    # 保存zip格式
    # logger.add(file, compression="zip")
    # 异步写入
    # logger.add("file", enqueue=True)
    # 序列化为json
    logger.add(file, serialize=True)
    logger.info("日志初始化成功...")


# 初始化日志相关配置
init_log()


class MyLogger:
    """
    日志配置
    """

    @staticmethod
    def get_log():
        return logger

    # 异常信息打印
    @staticmethod
    def log_error(params=None):
        exc_type, exc_value, exc_traceback = sys.exc_info()
        traceback_details = {
            "filename": exc_traceback.tb_frame.f_code.co_filename,
            "lineno": exc_traceback.tb_lineno,
            "name": exc_traceback.tb_frame.f_code.co_name,
            "type": exc_type.__name__,
            "message": exc_value
        }
        logger.error("{}-{}", params, traceback_details)
