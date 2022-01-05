# Author : lml
# Date : 2021/12/16


from enum import Enum


class ClickActionEnum(Enum):
    """
    点击动作的枚举类
    """

    JS = '使用js来点击'

    API = '使用原生的方法来触发点击'

    BY_TAG_TYPE = '根据标签类型决定'

    DOUBLE_CLICK = '双击'

    RIGHT_CLICK = '右键'

    @staticmethod
    def get_name_by_value(name: str):
        for enum_name, enum_val in ClickActionEnum.__members__.items():
            if name == enum_name:
                return enum_val
        raise ValueError(f'找不到{name}的枚举类')
