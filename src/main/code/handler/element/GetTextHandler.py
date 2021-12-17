# Author : lml
# Date : 2021/12/17
from loguru import logger

from src.main.code.enums.ActionEnum import ActionEnum
from src.main.code.handler.SeleniumHandler import SeleniumHandler


class GetTextHandler(SeleniumHandler):
    """
    查找文本处理器
    """

    def get_action(self) -> ActionEnum:
        return ActionEnum.getText

    def do_handle(self, ele_handle_dto: dict) -> None:
        element = ele_handle_dto['element'][0]
        by = ele_handle_dto['by']
        logger.info("查找文本:【{}】{}", by, element)

    def pre_handle(self, ele_handle_dto: dict) -> bool:
        return True
