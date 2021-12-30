# Author : lml
# Date : 2021/12/8
from enum import Enum


class ActionEnum(Enum):
    """
    selenium动作枚举类,value=true表示需要查找dom,false表示不用
    """

    # 点击动作
    CLICK = True

    # 双击动作
    DOUBLE_CLICK = True

    # 发送文字
    SEND_KEYS = True

    # 鼠标悬浮
    HOVER = True

    # 清空输入栏
    CLEAR = True

    # 切换iframe
    SWITCH_TO_FRAME = True

    # 点击alert
    ALERT = False

    # 等待
    WAIT = False

    # 运行js脚本
    RUN_SCRIPT = False

    # 刷新页面
    REFRESH = False

    # 通过反射调用对应的方法
    RUN_METHOD = False
