# Author : lml
# Date : 2021/12/8
from loguru import logger
from selenium.webdriver import ActionChains
from selenium.webdriver.remote.webelement import WebElement

from src.main.code.enums.ActionEnum import ActionEnum
from src.main.code.enums.ClickActionEnum import ClickActionEnum
from src.main.code.handler.element.ElementHandler import ElementHandler
from src.main.code.util.InitUtil import InitUtil
from src.main.code.util.JsUtil import JsUtil


class ClickHandler(ElementHandler):
    """
    点击的处理器
    """

    # 需要动态判断点击方式的元素元祖
    TAG_NAMES_CLICK_BY_JS = ("button", "a", "span", "img", "li", "input")

    def __init__(self) -> None:
        # 初始化好对应的点击方法
        self.do_click_func = {
            ClickActionEnum.API: self.__api_click,
            ClickActionEnum.JS: self.__js_click,
            ClickActionEnum.BY_TAG_TYPE: self.__by_tag,
            ClickActionEnum.RIGHT_CLICK: self.__right_click,
            ClickActionEnum.DOUBLE_CLICK: self.__double_click,
        }

    def get_action(self):
        return ActionEnum.CLICK

    def pre_handle(self, ele_handle_dto) -> bool:
        element = ele_handle_dto.elements[0]
        by = ele_handle_dto.by
        script = "var items = {}; for (index = 0; index < arguments[0].attributes.length; ++index) { items[arguments[0].attributes[index].name] = arguments[0].attributes[index].value }; return items;"
        result = JsUtil.run_js_with_param(script, element)
        logger.debug("click element attributes:{}", result)
        attribute = element.get_attribute('disabled')
        if not element.is_enabled() or 'true' == attribute:
            logger.warning('[{}]元素[{}]不是Enable状态，不能点击', by, element)
            return False
        return True

    def do_handle(self, ele_handle_dto) -> None:
        """
        处理点击事件
        :param ele_handle_dto: element:定位到的元素,by:定位的方式,clickActionEnum:点击的类型
        """
        element = ele_handle_dto.elements[0]
        by = ele_handle_dto.by
        click_action = ele_handle_dto.click_action
        self.do_click_func[click_action](element)
        logger.debug("使用{}点击元素:[{}]成功", by, element)

    @staticmethod
    def __api_click(ele: WebElement) -> None:
        logger.debug("使用原生的方法点击")
        ele.click()

    @staticmethod
    def __js_click(ele: WebElement) -> None:
        logger.debug("使用js来点击")
        JsUtil.run_js_with_param("arguments[0].click();", ele)

    def __by_tag(self, ele: WebElement) -> None:
        """
        根据元素的tag来动态判断使用哪种点击方法
        :param ele: 需要点击的元素
        """
        logger.debug("自动判断用哪一种点击")
        if ele.tag_name in self.TAG_NAMES_CLICK_BY_JS:
            self.__js_click(ele)
            return None
        self.__api_click(ele)

    @staticmethod
    def __right_click(ele: WebElement) -> None:
        ActionChains(InitUtil.get_driver()).context_click(ele).perform()

    @staticmethod
    def __double_click(ele: WebElement) -> None:
        ActionChains(InitUtil.get_driver()).double_click(ele).perform()
