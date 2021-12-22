# Author : lml
# Date : 2021/12/1
from loguru import logger
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from seleniumwire import webdriver

from src.main.code.config.GlobalConfig import GlobalConfig
from src.main.code.config.Logger import MyLogger
from src.main.code.dto.EleHandleDto import EleHandleDto
from src.main.code.exceptions.FindElementException import FindElementException
from src.main.code.handler.SeleniumHandler import SeleniumHandler
from src.main.code.util.JsUtil import JsUtil


class SeleniumUtil:
    """
    selenium工具类
    """

    selenium_driver = None

    # 初始化设置
    config = GlobalConfig.get_config()

    @classmethod
    def get_driver(cls):
        """
        初始化selenium的驱动并且返回
        :return: 初始化好的驱动
        """
        options = webdriver.ChromeOptions()
        # 禁用扩展
        options.add_argument('disable-extensions')
        # 禁用阻止弹出窗口
        options.add_argument('--disable-popup-blocking')
        # 设置这两个参数就可以避免密码提示框的弹出
        options.add_experimental_option('prefs', {
            'credentials_enable_service': False,
            'profile.password_manager_enabled': False
        })
        if cls.config['useNoHead']:
            # 浏览器不提供可视化页面
            options.add_argument('--headless')
        cls.selenium_driver = webdriver.Chrome(chrome_options=options, executable_path=cls.config['driverPath'])
        # 初始化js工具类的驱动
        JsUtil.init_driver(cls.selenium_driver)
        return cls.selenium_driver

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
        if cls.selenium_driver is not None:
            cls.selenium_driver.quit()

    @classmethod
    def find_element(cls, by: By, value: str) -> WebElement:
        """
        查找单个元素
        :param by:  元素定位的方式
        :param value:  需要查找的元素的路径
        :return: 如果查找到的元素有多个,默认返回第一个
        """
        return cls.retry_find_and_do(by=by, path=value)[0]

    @classmethod
    def click_ele(cls, by: By, path: str) -> None:
        """
        点击元素
        :param by:  元素定位的方式
        :param path: 需要点击的元素的路径
        """
        cls.retry_find_and_do(by=by, path=path)[0].click()

    @classmethod
    def retry_find_and_do(cls, **handle_dto) -> list:
        """
        重复查找和执行动作,会有重试机制
        :param handle_dto: 需要有查找的方式by和查找的路径path等属性
        :return: 返回查找到的元素
        """
        attempts = 0
        retry = cls.config['retry']
        by = handle_dto['by']
        path = handle_dto['path']
        selenium_handler = handle_dto.get('handler')
        while attempts <= retry:
            try:
                find_element = cls.__fluent_find(by, path)
                ele_handle_dto = cls.__build_ele_handle_dto(find_element, handle_dto)
                if selenium_handler is not None and isinstance(selenium_handler, SeleniumHandler) and selenium_handler.pre_handle(ele_handle_dto):
                    selenium_handler.do_handle(ele_handle_dto)
                return find_element
            except Exception:
                if attempts == retry:
                    msg = f'查找{by}【{path}】时尝试{attempts}次仍然发生错误'
                    MyLogger.log_error(msg)
                    raise FindElementException(msg)
                attempts = attempts + 1
                logger.warning('操作节点{}【{}】时,发生错误,重试第{}次', by, path, attempts)

    @classmethod
    def __build_ele_handle_dto(cls, find_element: list, handle_dto: dict) -> EleHandleDto:
        """
        构建eleHandleDto
        :param find_element: 查找到的元素列表
        :param handle_dto: 处理的传输类,需要有by,clickActionEnum,keys等元素
        :return: 返回构件好的dto
        """
        dto = EleHandleDto()
        dto.elements = find_element
        dto.by = handle_dto['by']
        dto.click_action = handle_dto.get('clickActionEnum')
        dto.keys = handle_dto.get('keys')
        return dto

    @classmethod
    def __fluent_find(cls, by: By, path: str) -> list:
        """
        使用显示的方式去查找元素
        :param by:  元素定位的方式
        :param path: 需要点击的元素的路径
        :return: 返回查找到的元素
        """
        wait_ele = WebDriverWait(cls.selenium_driver, cls.config['waitElement']).until(lambda browser: browser.find_elements(by, path))
        logger.info("元素:{},存在:{}", wait_ele, cls.is_find(wait_ele))
        return wait_ele

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
        cls.selenium_driver.refresh()

    @classmethod
    def click_alert(cls):
        """点击alert弹窗"""
        cls.selenium_driver.switch_to.alert.accept()
