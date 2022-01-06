# Author : lml
# Date : 2021/12/28

"""
文件说明
"""
import abc

from src.main.code.dto.EleHandlerDto import EleHandlerDto
from src.main.code.handler.SeleniumHandler import SeleniumHandler


class ElementHandler(SeleniumHandler):

    @abc.abstractmethod
    def do_handle(self, handle_dto: EleHandlerDto) -> None:
        pass

    @abc.abstractmethod
    def pre_handle(self, handle_dto: EleHandlerDto) -> bool:
        pass
