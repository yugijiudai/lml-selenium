# Author : lml
# Date : 2021/12/1

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from seleniumwire import webdriver

from src.main.code.config.Logger import MyLogger
from src.main.code.exceptions.FindElementException import FindElementException
from src.main.code.util.InitUtil import InitUtil

# 日志
log = MyLogger.get_log()


class SeleniumUtil:
    """
    selenium工具类
    """

    selenium_driver = None

    # 初始化设置
    setting = InitUtil.init_setting()

    @classmethod
    def get_driver(cls):
        """
        初始化selenium的驱动并且返回
        :return: 初始化好的驱动
        """
        options = webdriver.ChromeOptions()
        # options.add_argument('User-Agent=Mozilla/5.0 (Linux; U; Android 8.1.0; zh-cn; BLA-AL00 Build/HUAWEIBLA-AL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.132 MQQBrowser/8.9 Mobile Safari/537.36')
        # 浏览器不提供可视化页面
        # options.add_argument('--headless')
        # 禁用扩展
        options.add_argument('disable-extensions')
        # 禁用阻止弹出窗口
        options.add_argument('--disable-popup-blocking')
        # 设置这两个参数就可以避免密码提示框的弹出
        options.add_experimental_option('prefs', {
            'credentials_enable_service': False,
            'profile.password_manager_enabled': False
        })
        cls.selenium_driver = webdriver.Chrome(chrome_options=options, executable_path='/Volumes/common/dev/driver/chromedriver')
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
    def click_ele(cls, by: By, path: str):
        """
        点击元素
        :param by:  元素定位的方式
        :param path: 需要点击的元素的路径
        """
        cls.retry_find_and_do(by=by, path=path)[0].click()

    @classmethod
    def retry_find_and_do(cls, **handle_dto):
        """
        重复查找和执行动作,会有重试机制
        :param handle_dto: 需要有查找的方式by和查找的路径path
        :return: 返回查找到的元素
        """
        attempts = 0
        retry = cls.setting['retry']
        by = handle_dto['by']
        path = handle_dto['path']
        while attempts <= retry:
            try:
                find_element = cls.__fluent_find(by, path)
                if cls.pre_handle(find_element):
                    cls.do_handle()
                    return find_element
            except Exception:
                if attempts == retry:
                    msg = f'查找{by}【{path}】时尝试{attempts}次仍然发生错误'
                    MyLogger.except_info(msg)
                    raise FindElementException(msg)
                attempts = attempts + 1
                log.warning('操作节点{}【{}】时,发生错误,重试第{}次', by, path, attempts)

    @classmethod
    def __fluent_find(cls, by: By, path: str) -> list:
        """
        使用显示的方式去查找元素
        :param by:  元素定位的方式
        :param path: 需要点击的元素的路径
        :return: 返回查找到的元素
        """
        wait_ele = WebDriverWait(cls.selenium_driver, cls.setting['waitElement']).until(lambda browser: browser.find_elements(by, path))
        log.info("元素:{},存在:{}", wait_ele, cls.is_find(wait_ele))
        return wait_ele

    @classmethod
    def is_find(cls, elements: list) -> bool:
        """
        该元素是否可用
        :param elements: 查找到的元素
        :return: true表示可用
        """
        flag = False
        for find_ele in elements:
            flag = find_ele is not None and find_ele.is_displayed() and find_ele.is_enabled()
        return flag

    @classmethod
    def send_keys(cls, by: By, path: str, text: str):
        element = cls.find_element(by, path)
        element.send_keys(text)

    @classmethod
    def pre_handle(cls, ele: list) -> bool:
        return True

    @classmethod
    def do_handle(cls):
        pass