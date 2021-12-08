# Author : lml
# Date : 2021/12/8
from src.main.code.enums.ActionEnum import ActionEnum


class SeleniumHandler:
    """
    selenium处理器,用于处理各种事件
    """

    def get_action(self) -> ActionEnum:
        """
        :return: 事件的动作
        """
        pass

    def do_handle(self, ele_handle_dto: dict):
        pass

    def pre_handle(self, ele_handle_dto: dict) -> bool:
        pass
