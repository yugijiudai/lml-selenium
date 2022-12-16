# @Author:lml
# @Time:2021/12/6 22:07
# @File     :GlobalConfig.py
from src.main.code.exceptions.InitException import InitException


class GlobalConfig:
    """
    全局的配置文件
    """

    def __init__(self) -> None:
        raise InitException("该类不允许初始化")

    @staticmethod
    def get_config():
        """
        读取配置
        """
        return {
            # chromeDriver位置
            "driverPath": "/Volumes/common/dev/driver/chromedriver",
            # "driverPath": "D:\\driver\\chromedriver.exe",
            # 查找元素的重试次数
            "retry": 3,
            #  查找元素的时候等待元素的时间(显示等待,单位秒)
            "waitElement": 5,
            # 等待页面加载的最长时间(显示等待,单位秒)
            "pageLoad": 60,
            # 强制等待时间(单位秒)
            "waitTime": 0.5,
            # 是否最大化窗口，如果开启了窗口大小就会失效
            "isMax": False,
            # 是否打开浏览器
            "useNoHead": True,
            # 窗口的大小
            "windowSize": "1920,1080"
        }
