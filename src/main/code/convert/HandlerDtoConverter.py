# @Author:lml
# @Time:2022/1/6 23:32
# @File     :HandlerDtoConverter.py
from selenium.webdriver.common.by import By

from src.main.code.dto.EleHandlerDto import EleHandlerDto
from src.main.code.dto.HandlerDto import HandlerDto
from src.main.code.dto.NoEleHandlerDto import NoEleHandlerDto
from src.main.code.dto.SeleniumDto import SeleniumDto
from src.main.code.enums.ActionEnum import ActionEnum
from src.main.code.enums.ClickActionEnum import ClickActionEnum
from src.main.code.util.EnumUtil import EnumUtil
from src.main.code.util.JsonUtil import JsonUtil
from src.main.code.util.SeleniumUtil import SeleniumUtil
from src.main.code.util.StrUtil import StrUtil


class HandlerDtoConverter:
    """
    handlerDto转换工具类
    """

    @classmethod
    def build_handler_dto(cls, selenium_dto: SeleniumDto) -> HandlerDto:
        """
        构建eleHandleDto
        :param selenium_dto: 加载出来的用例dto
        :return: 返回构件好的dto
        """
        ext = JsonUtil.str_to_json(selenium_dto.ext) if JsonUtil.is_json(selenium_dto.ext) else ''
        action_enum = EnumUtil.convert_to_enum(selenium_dto.element_action, ActionEnum)
        # 判断是否需要查找节点
        if EnumUtil.get_enum_val(action_enum) is True:
            return cls.__build_ele_dto(ext, selenium_dto)
        return cls.__build_no_ele_dto(ext, selenium_dto)

    @staticmethod
    def __build_no_ele_dto(ext, selenium_dto):
        """
        构造不需要查找元素的dto
        :param ext: ext字段
        :param selenium_dto: 加载出来的用例dto
        :return: NoEleHandlerDto
        """
        no_ele = NoEleHandlerDto()
        no_ele.wait_time = selenium_dto.wait
        no_ele.ext = ext
        return no_ele

    @staticmethod
    def __build_ele_dto(ext, selenium_dto):
        """
        构造不需要查找元素的dto
        :param ext: ext字段
        :param selenium_dto: 加载出来的用例dto
        :return: EleHandlerDto
        """
        dto = EleHandlerDto()
        dto.by = getattr(By, selenium_dto.find_type) if StrUtil.is_not_blank(selenium_dto.find_type) else None
        dto.elements = SeleniumUtil.fluent_find(dto.by, selenium_dto.element)
        click_action = selenium_dto.click_action
        dto.click_action = EnumUtil.convert_to_enum(click_action, ClickActionEnum) if StrUtil.is_not_blank(click_action) else None
        dto.keys = ext
        return dto
