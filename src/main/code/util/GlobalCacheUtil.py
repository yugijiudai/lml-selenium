# @Author:lml
# @Time: 2022/1/10
# @File     :GlobalCacheUtil.py
from src.main.code.exceptions.InitException import InitException


class GlobalCacheUtil:

    def __init__(self) -> None:
        raise InitException("该类不允许初始化")

    # 全局的缓存
    __cache = {

    }

    @classmethod
    def set_cache(cls, key, val) -> None:
        """
        设置缓存
        :param key: 缓存的key
        :param val: 缓存的value
        """
        cls.__cache[key] = val

    @classmethod
    def get_cache(cls, key):
        """
        :param key:  缓存的key
        :return: 获取缓存
        """
        return cls.get_cache(key)
