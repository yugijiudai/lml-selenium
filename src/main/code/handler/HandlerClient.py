# Author : lml
# Date : 2021/12/30
from selenium.webdriver.common.by import By

from src.main.code.dto.selenium_dto import SeleniumDto
from src.main.code.enums.ClickActionEnum import ClickActionEnum
from src.main.code.factory.HandlerFactory import HandlerFactory
from src.main.code.util.JsonUtil import JsonUtil
from src.main.code.util.SeleniumUtil import SeleniumUtil
from src.main.code.util.StrUtil import StrUtil


class HandlerClient:
    """
    文件说明
    """

    def __init__(self) -> None:
        self.handler_dict = HandlerFactory.get_handler_dict()

    def do_action(self, selenium_dto: SeleniumDto):
        handler = self.handler_dict[selenium_dto.element_action]
        ext = JsonUtil.str_to_json(selenium_dto.ext) if JsonUtil.is_json(selenium_dto.ext) else ''
        by = getattr(By, selenium_dto.find_type) if StrUtil.is_not_blank(selenium_dto.find_type) else None
        click_action = ClickActionEnum.get_name_by_value(selenium_dto.click_action) if StrUtil.is_not_blank(selenium_dto.click_action) else None
        SeleniumUtil.find_or_handle(handler=handler, by=by, clickActionEnum=click_action,
                                    wait_time=selenium_dto.wait, ext=ext,
                                    keys=selenium_dto.ext, path=selenium_dto.element)
