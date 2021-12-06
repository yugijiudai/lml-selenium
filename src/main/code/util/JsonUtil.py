import json5


class JsonUtil:
    """
    json工具类
    """

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