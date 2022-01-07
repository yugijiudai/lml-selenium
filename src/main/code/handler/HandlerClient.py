# Author : lml
# Date : 2021/12/30
from src.main.code.dto.SeleniumDto import SeleniumDto
from src.main.code.factory.HandlerDtoFactory import HandlerDtoFactory
from src.main.code.factory.HandlerFactory import HandlerFactory


class HandlerClient:
    """
    调用handler的客户端
    """

    @staticmethod
    def do_action(selenium_dto: SeleniumDto) -> None:
        """
        根据用例提供的seleniumDto对象来动态调用对用的handler来处理相关的事件
        :param selenium_dto: 用例的对象
        """
        selenium_handler = HandlerFactory.get_handler_dict()[selenium_dto.element_action]
        handler_dto = HandlerDtoFactory.build_handler_dto(selenium_dto)
        if selenium_handler.pre_handle(handler_dto):
            selenium_handler.do_handle(handler_dto)
