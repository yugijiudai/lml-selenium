from src.main.code.dto.HandleDto import HandleDto
from src.main.code.enums.ClickActionEnum import ClickActionEnum


class EleHandleDto(HandleDto):
    """
    需要查找元素的dto
    """

    __slots__ = ('__elements', '__by', '__clickActionEnum', '__keys')

    def __init__(self):
        # 找到的元素list
        self.__elements = None
        # 查找的方式
        self.__by = None
        # 点击的动作枚举类
        self.__clickActionEnum = None
        # 输入的keys
        self.__keys = None

    @property
    def elements(self):
        return self.__elements

    @elements.setter
    def elements(self, value):
        self.__elements = value

    @property
    def by(self):
        return self.__by

    @by.setter
    def by(self, value):
        self.__by = value

    @property
    def click_action(self):
        if self.__clickActionEnum is not None:
            return self.__clickActionEnum
        return ClickActionEnum.by_tag_type

    @click_action.setter
    def click_action(self, value):
        self.__clickActionEnum = value

    @property
    def keys(self):
        return self.__keys

    @keys.setter
    def keys(self, value):
        self.__keys = value

    def to_dict(self):
        return {
            "elements": self.__elements,
            "by": self.__by,
            "clickActionEnum": self.__clickActionEnum,
            "keys": self.__keys,
        }
