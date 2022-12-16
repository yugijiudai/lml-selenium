# @Author:lml
# @Time:2021/12/6 23:46
# @File     :JsUtil.py
import time
from time import sleep

from loguru import logger
from selenium.webdriver.support.wait import WebDriverWait
from seleniumwire import webdriver

from src.main.code.config.GlobalConfig import GlobalConfig
from src.main.code.exceptions.FindElementException import FindElementException
from src.main.code.exceptions.InitException import InitException
from src.main.code.util.GlobalCacheUtil import GlobalCacheUtil
from src.main.code.util.ResourceUtil import ResourceUtil


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
    def init_driver(cls, driver: webdriver):
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
        logger.debug("预执行脚本:{}", script)
        response = cls.__js_driver.execute_script(script)
        logger.debug("执行脚本成功:{}\n返回值是:{}", script, response)
        return response

    @classmethod
    def run_js_with_param(cls, script: str, *kwargs):
        """
        执行js脚本,可以通过传参
        :param script:  需要运行的脚本
        :param kwargs:  需要传参
        :return: 脚本的返回值
        """
        logger.debug("预执行脚本:{}\n参数是:{}", script, *kwargs)
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
        # 先等一下确保请求有发送出去
        sleep(0.5)
        # 先等待JS加载完成
        cls.wait_until_js_ready()
        flag = cls.run_js("return typeof jQuery != 'undefined'")
        if not flag:
            logger.warning('页面不支持jQuery,尝试往里面添加...')
            cls.add_jq()
        cls.wait_until_ajax_load()

    @classmethod
    def load_common_script(cls, file_name: str) -> str:
        """
        加载common文件夹下的js
        :param file_name: js的名字
        :return: 加载出来的脚本
        """
        file = ResourceUtil.get_resource_path(f"script/common/{file_name}")
        return cls.load_script(file)

    @classmethod
    def load_script(cls, file_name: str) -> str:
        """
        给定指定的文件名字,去加载对应的js脚本
        :param file_name: 文件的路径
        :return: 加载出来的脚本
        """
        script_cache = GlobalCacheUtil.get_cache(file_name)
        if script_cache is not None:
            return script_cache
        script = ResourceUtil.load_file(file_name)
        GlobalCacheUtil.set_cache(file_name, script)
        return script

    @classmethod
    def add_jq(cls) -> None:
        """
        给页面添加jquery,如果添加不成功,则会抛出异常
        """
        cls.add_common('jq-min.js')
        flag = cls.run_js("return typeof jQuery != 'undefined'")
        if not flag:
            raise InitException("页面不支持jQuery!无法添加")

    @classmethod
    def add_common(cls, script) -> None:
        """
        添加common文件夹里的脚本
        :param script: 脚本的名字
        """
        script = cls.load_common_script(script)
        cls.run_js(script)
        cls.wait_until_js_ready()

    @classmethod
    def wait_page_load_by_js(cls, script, max_wait_time=__config['pageLoad'], wait_time=__config['waitTime']) -> None:
        """
        根据自定义的js设置等待
        :param script: 自定义的js
        :param max_wait_time: 最大等待时间
        :param wait_time: 轮询的时间
        """
        start = time.time()
        while cls.run_js(script) is False:
            if time.time() - start > max_wait_time:
                logger.warning("超出等待最长时间:{},跳出循环", max_wait_time)
                raise FindElementException(f"超出等待时间:{max_wait_time}")
            sleep(wait_time)

    @classmethod
    def run_dom_js(cls, call) -> None:
        """
        先注入domHelper.js,然后运行能调用domHelper里面函数的脚本
        :param call: 需要运行的脚本
        """
        cls.add_common('domHelper.js')
        cls.run_js(call)
