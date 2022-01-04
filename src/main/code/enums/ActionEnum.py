# Author : lml
# Date : 2021/12/8
from enum import Enum


class ActionEnum(Enum):
    """
    selenium动作枚举类,val=true表示需要查找dom,false表示不用
    """

    # 点击动作
    CLICK = Enum('CLICK', [('val', True)])

    # 双击动作
    DOUBLE_CLICK = Enum('DOUBLE_CLICK', [('val', True)])

    # 发送文字
    SEND_KEYS = Enum('SEND_KEYS', [('val', True)])

    # 鼠标悬浮
    HOVER = Enum('HOVER', [('val', True)])

    # 清空输入栏
    CLEAR = Enum('CLEAR', [('val', True)])

    # 切换iframe
    SWITCH_TO_FRAME = Enum('SWITCH_TO_FRAME', [('val', True)])

    # 点击alert
    ALERT = Enum('ALERT', [('val', False)])

    # 等待
    WAIT = Enum('WAIT', [('val', False)])

    # 运行js脚本
    RUN_SCRIPT = Enum('RUN_SCRIPT', [('val', False)])

    # 刷新页面
    REFRESH = Enum('REFRESH', [('val', False)])

    # 通过反射调用对应的方法
    RUN_METHOD = Enum('RUN_METHOD', [('val', False)])
