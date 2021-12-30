# Author : lml
# Date : 2021/12/17
from selenium.webdriver import ActionChains

from src.main.code.enums.ActionEnum import ActionEnum
from src.main.code.handler.element.ElementHandler import ElementHandler
from src.main.code.util.InitUtil import InitUtil


class HoverHandler(ElementHandler):
    """
    鼠标停留处理器
    """

    def get_action(self) -> ActionEnum:
        return ActionEnum.HOVER

    def do_handle(self, ele_handle_dto) -> None:
        element = ele_handle_dto.elements[0]
        ActionChains(InitUtil.get_driver()).move_to_element(element).perform()

    def pre_handle(self, ele_handle_dto) -> bool:
        return True
