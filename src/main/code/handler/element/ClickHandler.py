# Author : lml
# Date : 2021/12/8
from loguru import logger

from src.main.code.enums.ActionEnum import ActionEnum
from src.main.code.handler.SeleniumHandler import SeleniumHandler
from src.main.code.util.JsUtil import JsUtil


class ClickHandler(SeleniumHandler):

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

    def do_handle(self, ele_handle_dto: dict):
        super().do_handle(ele_handle_dto)
