# Author : lml
# Date : 2021/12/8
import abc

from src.main.code.dto.HandleDto import HandleDto
from src.main.code.enums.ActionEnum import ActionEnum


class SeleniumHandler:
    """
    selenium处理器,用于处理各种事件
    """

    @abc.abstractmethod
    def get_action(self) -> ActionEnum:
        """
        :return: 事件的动作
        """
        pass

    @abc.abstractmethod
    def do_handle(self, handle_dto: HandleDto) -> None:
        pass

    @abc.abstractmethod
    def pre_handle(self, handle_dto: HandleDto) -> bool:
        pass
