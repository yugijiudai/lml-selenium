# @Author:lml
# @Time:2021/12/6 23:46
# @File     :JsUtil.py
from loguru import logger
from selenium.webdriver.support.wait import WebDriverWait

from src.main.code.config.GlobalConfig import GlobalConfig
from src.main.code.exceptions.InitException import InitException


class JsUtil:
    """
    文件说明：js工具类
    """
    __js_driver = None

    # 这个config不能用seleniumUtil的,不然会出现循环import导致报错
    __config = GlobalConfig.get_config()

    def __init__(self) -> None:
        raise InitException("该类不允许初始化")

    @classmethod
    def init_driver(cls, driver):
        """
        初始化工具类的驱动
        """
        cls.__js_driver = driver

    @classmethod
    def run_js(cls, script: str):
        """
        执行js脚本
        :param script:  需要运行的脚本
        :return: 脚本的返回值
        """
        logger.debug("与执行脚本:\n{}", script)
        response = cls.__js_driver.execute_script(script)
        logger.debug("执行脚本成功:\n{}\n返回值是:{}", script, response)
        return response

    @classmethod
    def run_js_with_param(cls, script: str, *kwargs):
        """
        执行js脚本,可以通过传参
        :param script:  需要运行的脚本
        :param kwargs:  需要传参
        :return: 脚本的返回值
        """
        logger.debug("与执行脚本:{}\n参数是:{}", script, *kwargs)
        response = cls.__js_driver.execute_script(script, *kwargs)
        logger.debug("执行脚本成功:{}\n参数是:{}\n返回值是:{}", script, *kwargs, response)
        return response

    @classmethod
    def wait_until_js_ready(cls) -> None:
        """
        等待页面的js加载完成
        """
        WebDriverWait(cls.__js_driver, cls.__config['pageLoad']).until(lambda browser: "complete" == cls.run_js("return document.readyState"))

    @classmethod
    def wait_until_ajax_load(cls) -> None:
        """
        等待ajax请求完成
        """
        WebDriverWait(cls.__js_driver, cls.__config['pageLoad']).until(lambda browser: cls.run_js("return jQuery.active==0"))

    @classmethod
    def wait_page_load(cls) -> None:
        """
        等待整个页面加载完成
        """
        # 先等待JS加载完成
        cls.wait_until_js_ready()
        flag = cls.run_js("return typeof jQuery != 'undefined'")
        if not flag:
            raise Exception('页面不支持jQuery')
        cls.wait_until_ajax_load()
