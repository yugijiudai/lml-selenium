# Author : lml
# Date : 2021/12/30
from src.main.code.dto.selenium_dto import SeleniumDto
from src.main.code.factory.HandlerFactory import HandlerFactory
from src.main.code.util.JsonUtil import JsonUtil
from src.main.code.util.SeleniumUtil import SeleniumUtil


class HandlerClient:
    """
    文件说明
    """

    def __init__(self) -> None:
        self.handler_dict = HandlerFactory.get_handler_dict()

    def do_action(self, selenium_dto: SeleniumDto):
        handler = self.handler_dict[selenium_dto.element_action]
        ext = JsonUtil.str_to_json(selenium_dto.ext) if JsonUtil.is_json(selenium_dto.ext) else ''
        SeleniumUtil.retry_find_and_do(handler=handler, by=selenium_dto.find_type,
                                       clickActionEnum=selenium_dto.click_action,
                                       wait_time=selenium_dto.wait, ext=ext,
                                       keys=selenium_dto.ext, path=selenium_dto.element)
        # print(selenium_dto.element_action == ActionEnum.CLICK.name)
        # print(ActionEnum[str(selenium_dto.element_action)])
        # print(selenium_dto.element_action)
