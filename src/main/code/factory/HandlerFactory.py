# Author : lml
# Date : 2022/1/4

from src.main.code.handler.element.ElementHandler import ElementHandler
from src.main.code.handler.other.NoElementHandler import NoElementHandler
from src.main.code.util.EnumUtil import EnumUtil
from src.main.code.util.ReflectUtil import ReflectUtil


class HandlerFactory:
    """
    handler的工厂类,用来初始化selenium的所有handler
    """
    # key是对应的actionEnum, value是handler的实例化对象
    __handler_dict = {}

    @classmethod
    def get_handler_dict(cls):
        return cls.__handler_dict

    @classmethod
    def init_all_handler(cls):
        """
        初始化所有handler
        :return:
        """
        ele_set = cls.init_ele_handler()
        no_ele_set = cls.init_no_ele_handler()
        ele_set.update(no_ele_set)
        for tmp in ele_set:
            handler = tmp()
            action = EnumUtil.get_enum_name(handler.get_action())
            cls.__handler_dict[action] = handler

    @classmethod
    def init_ele_handler(cls) -> set:
        """
        初始化需要查找元素的handler
        :return: ElementHandler的子类set
        """
        return ReflectUtil.get_sub(ElementHandler, ['src.main.code.handler.element'])

    @classmethod
    def init_no_ele_handler(cls) -> set:
        """
        初始化不需要查找元素的handler
        :return: NoElementHandler的子类set
        """
        return ReflectUtil.get_sub(NoElementHandler, ['src.main.code.handler.other'])
