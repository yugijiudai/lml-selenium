# Author : lml
# Date : 2021/12/29
from seleniumwire import webdriver

from src.main.code.config.GlobalConfig import GlobalConfig
from src.main.code.exceptions.InitException import InitException
from src.main.code.util.JsUtil import JsUtil


class InitUtil:
    """
    初始化工具类，用来初始化webDriver,并且把driver给与jsUtil
    """

    # selenium的驱动
    __selenium_driver = None

    def __init__(self) -> None:
        raise InitException("该类不允许初始化")

    @classmethod
    def get_driver(cls):
        return cls.__selenium_driver

    @classmethod
    def init_driver(cls) -> None:
        """
        初始化selenium的驱动并且返回
        :return: 初始化好的驱动，用户可以根据自己需要来使用，原则上不建议直接使用这个driver
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
        config = GlobalConfig.get_config()
        if config['useNoHead']:
            # 浏览器不提供可视化页面
            options.add_argument('--headless')
        cls.__selenium_driver = webdriver.Chrome(chrome_options=options, executable_path=config['driverPath'])
        # 初始化js工具类的驱动
        JsUtil.init_driver(cls.__selenium_driver)

    @classmethod
    def close_driver(cls):
        """
        关闭driver
        """
        if cls.__selenium_driver is not None:
            cls.__selenium_driver.quit()
