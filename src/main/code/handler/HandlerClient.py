# Author : lml
# Date : 2021/12/30
from src.main.code.dto.SeleniumDto import SeleniumDto
from src.main.code.factory.HandlerDtoFactory import HandlerDtoFactory
from src.main.code.factory.HandlerFactory import HandlerFactory
from src.main.code.handler.SeleniumHandler import SeleniumHandler


class HandlerClient:
    """
    调用handler的客户端
    """

    def __init__(self) -> None:
        self.handler_dict = HandlerFactory.get_handler_dict()

    def do_action(self, selenium_dto: SeleniumDto):
        """
        根据用例提供的seleniumDto对象来动态调用对用的handler来处理相关的事件
        :param selenium_dto:
        :return:
        """
        selenium_handler = self.handler_dict[selenium_dto.element_action]
        handler_dto = HandlerDtoFactory.build_handler_dto(selenium_dto)
        if isinstance(selenium_handler, SeleniumHandler) and selenium_handler.pre_handle(handler_dto):
            selenium_handler.do_handle(handler_dto)
