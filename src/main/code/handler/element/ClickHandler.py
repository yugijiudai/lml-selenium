# Author : lml
# Date : 2021/12/8
from loguru import logger
from selenium.webdriver import ActionChains
from selenium.webdriver.remote.webelement import WebElement

from src.main.code.enums.ActionEnum import ActionEnum
from src.main.code.enums.ClickActionEnum import ClickActionEnum
from src.main.code.handler.SeleniumHandler import SeleniumHandler
from src.main.code.util.JsUtil import JsUtil
from src.main.code.util.SeleniumUtil import SeleniumUtil


class ClickHandler(SeleniumHandler):
    """
    点击的处理器
    """

    # 需要动态判断点击方式的元素元祖
    TAG_NAMES_CLICK_BY_JS = ("button", "a", "span", "img", "li", "input")

    def get_action(self):
        return ActionEnum.click

    def pre_handle(self, ele_handle_dto: dict) -> bool:
        element = ele_handle_dto['element'][0]
        by = ele_handle_dto['by']
        script = "var items = {}; for (index = 0; index < arguments[0].attributes.length; ++index) { items[arguments[0].attributes[index].name] = arguments[0].attributes[index].value }; return items;"
        result = JsUtil.run_js_with_param(script, element)
        logger.debug("click element attributes:{}", result)
        attribute = element.get_attribute('disabled')
        if not element.is_enabled() or 'true' == attribute:
            logger.warning('元素[{}]不是Enable状态，不能点击', by)
            return False
        return True

    def do_handle(self, ele_handle_dto: dict) -> None:
        element = ele_handle_dto['element'][0]
        by = ele_handle_dto['by']
        click_action_enum = ele_handle_dto['clickActionEnum']
        self.__click_ele(click_action_enum, element)
        logger.debug("点击元素:[{}]成功", by)

    def __click_ele(self, click_action_enum: ClickActionEnum, ele: WebElement) -> None:
        """
        点击元素
        :param click_action_enum: 点击动作的枚举类
        :param ele: 需要点击的元素
        """
        if click_action_enum == ClickActionEnum.api:
            self.__api_click(ele)
        elif click_action_enum == ClickActionEnum.js:
            self.__js_click(ele)
        elif click_action_enum == ClickActionEnum.by_tag_type:
            self.__by_tag(ele)
        elif click_action_enum == ClickActionEnum.right_click:
            self.__right_click(ele)
        elif click_action_enum == ClickActionEnum.double_click:
            self.__double_click(ele)

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
        ActionChains(SeleniumUtil.selenium_driver).context_click(ele).perform()

    @staticmethod
    def __double_click(ele: WebElement) -> None:
        ActionChains(SeleniumUtil.selenium_driver).double_click(ele).perform()
