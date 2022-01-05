import json5

from src.main.code.exceptions.InitException import InitException


class JsonUtil:
    """
    json工具类
    """

    def __init__(self) -> None:
        raise InitException("该类不允许初始化")

    @staticmethod
    def to_json_str(obj):
        """
        转成json格式
        :param obj:  需要转换的对象
        :return: json类型的字符串
        """
        return json5.dumps(obj, ensure_ascii=False, quote_keys=True)

    @staticmethod
    def str_to_json(text: str) -> json5:
        """
        str转json
        @param text: 需要转json的字符串
        @return: json格式
        """
        return json5.loads(text)

    @staticmethod
    def set_not_null_val(target: dict, source: dict, pro: str):
        """
        如果源对象的属性非空则设置这个属性到新的对象
        @param target: 目标对象
        @param source: 源对象
        @param pro: 属性的key
        """
        val = source.get(pro)
        if val is not None:
            target[pro] = val

    @staticmethod
    def get_default(dict_obj: dict, key: str, default_val):
        """
        根据key来获取dict的value,如果key为空,则获取默认的值
        :param dict_obj: 对应的dict
        :param key: dict的key
        :param default_val: 如果key不存在,则默认获取的值
        :return: 对应的value
        """
        return dict_obj[key] if dict_obj.get(key) is not None else default_val

    @classmethod
    def is_json(cls, content):
        try:
            cls.str_to_json(content)
        except ValueError:
            return False
        return True
