# Author : lml
# Date : 2021/12/30
from selenium.webdriver.common.by import By

from src.main.code.dto.EleHandleDto import EleHandleDto
from src.main.code.dto.HandleDto import HandleDto
from src.main.code.dto.NoEleHandleDto import NoEleHandleDto
from src.main.code.dto.SeleniumDto import SeleniumDto
from src.main.code.factory.HandlerFactory import HandlerFactory
from src.main.code.handler.SeleniumHandler import SeleniumHandler
from src.main.code.util.EnumUtil import EnumUtil
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
        selenium_handler = self.handler_dict[selenium_dto.element_action]
        handler_dto = self.__build_handle_dto(selenium_dto)
        if isinstance(selenium_handler, SeleniumHandler) and selenium_handler.pre_handle(handler_dto):
            selenium_handler.do_handle(handler_dto)
        # ext = JsonUtil.str_to_json(selenium_dto.ext) if JsonUtil.is_json(selenium_dto.ext) else ''
        # by = getattr(By, selenium_dto.find_type) if StrUtil.is_not_blank(selenium_dto.find_type) else None
        # click_action = ClickActionEnum.get_name_by_value(selenium_dto.click_action) if StrUtil.is_not_blank(selenium_dto.click_action) else None
        # SeleniumUtil.find_or_handle(handler=handler, by=by, clickActionEnum=click_action, wait_time=selenium_dto.wait, ext=ext, keys=selenium_dto.ext, path=selenium_dto.element)

    @classmethod
    def __build_handle_dto(cls, selenium_dto: SeleniumDto) -> HandleDto:
        """
        构建eleHandleDto
        :param selenium_dto: 加载出来的用例dto
        :return: 返回构件好的dto
        """
        ext = JsonUtil.str_to_json(selenium_dto.ext) if JsonUtil.is_json(selenium_dto.ext) else ''
        action_enum = selenium_dto.element_action
        # 判断是否需要查找节点
        if EnumUtil.get_enum_val(action_enum) is True:
            dto = EleHandleDto()
            dto.by = getattr(By, selenium_dto.find_type) if StrUtil.is_not_blank(selenium_dto.find_type) else None
            dto.elements = SeleniumUtil.fluent_find(dto.by, selenium_dto.element)
            dto.click_action = selenium_dto.click_action
            dto.keys = ext
            return dto
        no_ele = NoEleHandleDto()
        no_ele.wait_time = selenium_dto.wait
        no_ele.ext = ext
        return no_ele
