# @Author:lml
# @Time:2022/1/4 23:23
# @File     :EnumUtil.py
from enum import Enum


class EnumUtil:
    """
   枚举工具类

    """

    @staticmethod
    def get_enum_name(enum: Enum) -> str:
        """
        :param enum: 枚举对象
        :return: 获取枚举的name
        """
        return enum.name

    @staticmethod
    def get_enum_val(enum: Enum, val_tag='val'):
        """
        :param enum: 枚举对象
        :param val_tag: 枚举value的自定义key
        :return: 获取枚举的value
        """
        return enum.value[val_tag].value

    @classmethod
    def get_all(cls, enum, val_tag='val'):
        """
        :param enum: 枚举对象
        :param val_tag: 枚举value的自定义key
        :return: 获取枚举的所有key和value,变成list返回
        """
        enum_list = []
        for tmp in enum.__members__.items():
            key = cls.get_enum_name(tmp[1])
            value = cls.get_enum_val(tmp[1], val_tag)
            enum_list.append({key: value})
        return enum_list
