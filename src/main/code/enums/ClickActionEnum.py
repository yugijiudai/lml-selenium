# Author : lml
# Date : 2021/12/16


from enum import Enum


class ClickActionEnum(Enum):
    """
    点击动作的枚举类
    """

    js = '使用js来点击'

    api = '使用原生的方法来触发点击'

    by_tag_type = '根据标签类型决定'

    double_click = '双击'

    right_click = '右键'
