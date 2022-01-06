# Author : lml
# Date : 2021/12/1
from time import sleep

from loguru import logger
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait

from src.main.code.config.GlobalConfig import GlobalConfig
from src.main.code.config.Logger import MyLogger
from src.main.code.dto.EleHandlerDto import EleHandlerDto
from src.main.code.dto.HandlerDto import HandlerDto
from src.main.code.dto.NoEleHandlerDto import NoEleHandlerDto
from src.main.code.exceptions.FindElementException import FindElementException
from src.main.code.exceptions.InitException import InitException
from src.main.code.handler.SeleniumHandler import SeleniumHandler
from src.main.code.util.EnumUtil import EnumUtil
from src.main.code.util.InitUtil import InitUtil


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

    @staticmethod
    def get_request_msg(web_driver):
        for request in web_driver.requests:
            if request.response:
                print(request)

    @classmethod
    def close_driver(cls):
        """
        关闭driver
        """
        if InitUtil.get_driver() is not None:
            InitUtil.get_driver().quit()

    @classmethod
    def find_element(cls, by: By, value: str) -> WebElement:
        """
        查找单个元素
        :param by:  元素定位的方式
        :param value:  需要查找的元素的路径
        :return: 如果查找到的元素有多个,默认返回第一个
        """
        return cls.fluent_find(by=by, path=value)[0]

    @classmethod
    def click_ele(cls, by: By, path: str) -> None:
        """
        点击元素
        :param by:  元素定位的方式
        :param path: 需要点击的元素的路径
        """
        cls.fluent_find(by=by, path=path)[0].click()

    @classmethod
    def find_or_handle(cls, **handle_dto) -> list:
        """
        查找元素或者根据handler来出来，如果handler为空,则只纯去查找元素
        :param handle_dto: 需要有查找的方式by和查找的路径path等属性
        :return: 返回查找到的元素
        """
        by = handle_dto.get('by')
        path = handle_dto.get('path')
        selenium_handler = handle_dto.get('handler')
        if selenium_handler is None:
            return cls.fluent_find(by, path)
        handler_dto = cls.__build_handle_dto(handle_dto)
        if isinstance(selenium_handler, SeleniumHandler) and selenium_handler.pre_handle(handler_dto):
            selenium_handler.do_handle(handler_dto)
        if isinstance(handler_dto, EleHandlerDto) is True:
            return handler_dto.elements

    @classmethod
    def __build_handle_dto(cls, handle_dto: dict) -> HandlerDto:
        """
        构建eleHandleDto
        :param handle_dto: 处理的传输类,需要有by,clickActionEnum,keys等元素
        :return: 返回构件好的dto
        """
        selenium_handler = handle_dto['handler']
        action_enum = selenium_handler.get_action()
        # 判断是否需要查找节点
        if EnumUtil.get_enum_val(action_enum) is True:
            dto = EleHandlerDto()
            dto.by = handle_dto['by']
            dto.elements = cls.fluent_find(dto.by, handle_dto['path'])
            dto.click_action = handle_dto.get('clickActionEnum')
            dto.keys = handle_dto.get('keys')
            return dto
        no_ele = NoEleHandlerDto()
        no_ele.wait_time = handle_dto.get('wait_time')
        no_ele.ext = handle_dto.get('ext')
        return no_ele

    @classmethod
    def fluent_find(cls, by: By, path: str) -> list:
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
