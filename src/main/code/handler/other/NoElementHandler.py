# Author : lml
# Date : 2021/12/28

import abc

from src.main.code.dto.NoEleHandlerDto import NoEleHandlerDto
from src.main.code.handler.SeleniumHandler import SeleniumHandler


class NoElementHandler(SeleniumHandler):

    @abc.abstractmethod
    def do_handle(self, handle_dto: NoEleHandlerDto) -> None:
        pass

    @abc.abstractmethod
    def pre_handle(self, handle_dto: NoEleHandlerDto) -> bool:
        pass
