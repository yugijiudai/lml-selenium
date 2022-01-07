# @Author:lml
# @Time:2022/1/5 23:57
# @File     :StrUtil.py
from src.main.code.exceptions.InitException import InitException


class StrUtil:
    """
    字符串工具类
    """

    def __init__(self) -> None:
        raise InitException("该类不允许初始化")

    @staticmethod
    def is_blank(value) -> bool:
        """
        :param value: 要判断的字符串
        :return: 判断字符串是否为空
        """
        if value is None:
            return True
        if type(value) is not str:
            raise ValueError('传入的不是字符串')
        return value == ''

    @classmethod
    def is_not_blank(cls, value) -> bool:
        """
        :param value: 要判断的字符串
        :return: 判断字符串是否非空
        """
        return not cls.is_blank(value)
