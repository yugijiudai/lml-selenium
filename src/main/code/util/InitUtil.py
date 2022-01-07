# Author : lml
# Date : 2021/12/29
from seleniumwire import webdriver

from src.main.code.config.GlobalConfig import GlobalConfig
from src.main.code.dto.SeleniumDto import SeleniumDto
from src.main.code.exceptions.InitException import InitException
from src.main.code.factory.HandlerFactory import HandlerFactory
from src.main.code.util.DbUtil import DbUtil
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
    def init_all(cls) -> None:
        """
        初始化所有内容
        """
        # 初始化selenium的驱动
        cls.__selenium_driver = cls.__init_driver()
        # 初始化js工具类的驱动
        cls.__init_js_driver(cls.__selenium_driver)
        cls.__init_handler()

    @classmethod
    def __init_driver(cls) -> webdriver:
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
        driver = webdriver.Chrome(chrome_options=options, executable_path=config['driverPath'])
        if config['isMax']:
            driver.maximize_window()
        return driver

    @classmethod
    def __init_js_driver(cls, driver: webdriver) -> None:
        """
        初始化jsUtil里面的驱动
        :param driver: webdriver
        """
        JsUtil.init_driver(driver)

    @classmethod
    def __init_handler(cls) -> None:
        """
        初始化所有的handler
        """
        HandlerFactory.init_all_handler()

    @staticmethod
    def load_test_case(table_name: str, model_name: str) -> list:
        """
        根据模块加载对应的用例
        :param table_name: 表的名字
        :param model_name: 模块名字
        :return: 返回对应的seleniumDto列表
        """
        conn = DbUtil.get_conn()
        result = DbUtil.query_list(conn, "select * from " + table_name + " where model = %s and valid = 'Y' order by id", (model_name))
        result_list = []
        for row in result:
            dto = SeleniumDto()
            dto.id = row.get('id')
            dto.description = row.get('description')
            dto.model = row.get('model')
            dto.element_action = row.get('elementAction')
            dto.click_action = row.get('clickAction')
            dto.element = row.get('element')
            dto.find_type = row.get('findType')
            dto.ext = row.get('ext')
            dto.call_back = row.get('callBack')
            dto.wait = row.get('wait')
            dto.retry = row.get('retry')
            result_list.append(dto)
        DbUtil.close_conn(conn)
        return result_list

    @classmethod
    def close_driver(cls):
        """
        关闭driver
        """
        if cls.__selenium_driver is not None:
            cls.__selenium_driver.quit()
