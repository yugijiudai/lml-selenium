# Author : lml
# Date : 2021/12/8
from enum import Enum


class ActionEnum(Enum):
    """
    selenium动作枚举类,value=true表示需要查找dom,false表示不用
    """

    # 点击动作
    click = True

    # 双击动作
    doubleClick = True

    # 发送文字
    sendKeys = True

    # 鼠标悬浮
    hover = True

    # 获取文本内容
    getText = True

    # 清空输入栏
    clear = True

    # 切换iframe
    switchToFrame = True


    # 点击alert
    alert = False

    # 等待
    wait = False

    # 运行js脚本
    runScript = False

    # 刷新页面
    refresh = False

    # 通过反射调用对应的方法
    runMethod = False
