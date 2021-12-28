# Author : lml
# Date : 2021/12/17
from src.main.code.enums.ActionEnum import ActionEnum
from src.main.code.handler.element.ElementHandler import ElementHandler


class ClearHandler(ElementHandler):
    """
    清空输入栏处理器
    """

    def get_action(self) -> ActionEnum:
        return ActionEnum.clear

    def do_handle(self, ele_handle_dto) -> None:
        element = ele_handle_dto.elements[0]
        element.clear()

    def pre_handle(self, ele_handle_dto) -> bool:
        return True
