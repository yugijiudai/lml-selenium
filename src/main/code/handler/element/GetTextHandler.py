# Author : lml
# Date : 2021/12/17
from loguru import logger

from src.main.code.enums.ActionEnum import ActionEnum
from src.main.code.handler.element.ElementHandler import ElementHandler


class GetTextHandler(ElementHandler):
    """
    查找文本处理器
    """

    def get_action(self) -> ActionEnum:
        return ActionEnum.getText

    def do_handle(self, ele_handle_dto) -> None:
        element = ele_handle_dto.elements[0]
        by = ele_handle_dto.by
        logger.info("使用{}查找文本:【{}】{}", by, element.get_attribute('innerText'), element)

    def pre_handle(self, ele_handle_dto) -> bool:
        return True
