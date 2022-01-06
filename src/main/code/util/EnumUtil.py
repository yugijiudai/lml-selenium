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

    @staticmethod
    def convert_to_enum(val: str, enum) -> Enum:
        """
        :param val: 需要转换的值
        :param enum: 最终转换出去的枚举类
        :return: 根据字符串的值转换成对应的枚举类
        """
        for enum_name, enum_val in enum.__members__.items():
            if val == enum_name:
                return enum_val
        raise ValueError(f'找不到{val}的枚举类')
