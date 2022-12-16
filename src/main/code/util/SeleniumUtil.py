# Author : lml
# Date : 2021/12/1
from time import sleep

from loguru import logger
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait

from src.main.code.config.GlobalConfig import GlobalConfig
from src.main.code.config.Logger import MyLogger
from src.main.code.exceptions.FindElementException import FindElementException
from src.main.code.exceptions.InitException import InitException
from src.main.code.util.InitUtil import InitUtil
from src.main.code.util.JsUtil import JsUtil


class SeleniumUtil:
    """
    selenium工具类
    """

    # 初始化设置
    __config = GlobalConfig.get_config()

    def __init__(self) -> None:
        raise InitException("该类不允许初始化")

    @classmethod
    def get_url(cls, url) -> None:
        """
        打开对应的url
        :param url: 要打开的地址
        """
        InitUtil.get_driver().get(url)

    @classmethod
    def close_driver(cls):
        """
        关闭driver
        """
        if InitUtil.get_driver() is not None:
            InitUtil.get_driver().quit()

    @classmethod
    def find_element(cls, by: By, path: str) -> WebElement:
        """
        查找单个元素
        :param by:  元素定位的方式
        :param path:  需要查找的元素的路径
        :return: 如果查找到的元素有多个,默认返回第一个
        """
        return cls.find_elements(by=by, path=path)[0]

    @classmethod
    def find_elements(cls, by: By, path: str) -> list:
        """
        查找多个元素
        :param by:  元素定位的方式
        :param path:  需要查找的元素的路径
        :return: 找到的元素列表
        """
        return cls.__fluent_find(by=by, path=path)

    @classmethod
    def click_ele(cls, by: By, path: str) -> None:
        """
        点击元素
        :param by:  元素定位的方式
        :param path: 需要点击的元素的路径
        """
        ele = cls.__fluent_find(by=by, path=path)[0]
        # ele.click()
        JsUtil.run_js_with_param("arguments[0].click();", ele)

    @classmethod
    def __fluent_find(cls, by: By, path: str) -> list:
        """
        重复查找和执行动作,会有重试机制
        :param by: 元素定位的方式
        :param path: 需要查找的元素路径
        :return: 返回查找到的元素
        """
        attempts = 0
        retry = cls.__config['retry']
        while attempts <= retry:
            try:
                wait_ele = WebDriverWait(InitUtil.get_driver(), cls.__config['waitElement']).until(lambda browser: browser.find_elements(by, path))
                logger.info("元素:{},存在:{}", wait_ele, cls.is_find(wait_ele))
                return wait_ele
            except Exception:
                if attempts == retry:
                    msg = f'查找{by}【{path}】时尝试{attempts}次仍然发生错误'
                    MyLogger.log_error(msg)
                    raise FindElementException(msg)
                attempts = attempts + 1
                logger.warning('操作节点{}【{}】时,发生错误,重试第{}次', by, path, attempts)

    @classmethod
    def is_find(cls, elements: list) -> bool:
        """
        该元素是否可用
        :param elements: 查找到的元素
        :return: true表示可用
        """
        for find_ele in elements:
            if find_ele is None or not find_ele.is_displayed() or not find_ele.is_enabled():
                return False
        return True

    @classmethod
    def send_keys(cls, by: By, path: str, text: str) -> None:
        element = cls.find_element(by, path)
        # 先点中,然后清空,最后输入
        element.click()
        element.clear()
        element.send_keys(text)

    @classmethod
    def refresh(cls):
        """刷新页面"""
        InitUtil.get_driver().refresh()

    @classmethod
    def click_alert(cls):
        """点击alert弹窗"""
        InitUtil.get_driver().switch_to.alert.accept()

    @staticmethod
    def do_wait(time=__config['waitTime']) -> None:
        """
        强制等待
        :param time: 单位秒
        """
        sleep(time)
