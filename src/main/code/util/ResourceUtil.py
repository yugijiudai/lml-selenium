import os

from src.main.code.exceptions.InitException import InitException

PROJECT_NAME = 'lml-selenium'


class ResourceUtil:
    """
    资源的工具类
    """

    def __init__(self) -> None:
        raise InitException("该类不允许初始化")

    @staticmethod
    def get_resource_path(path: str) -> str:
        """
        获取Resources目录里的资源
        :param path: 需要获取的文件相对路径
        :return: 返回文件的绝对路径
        """
        root_path = ResourceUtil.get_root_path()
        return f"{root_path}/src/main/resources/{path}"

    @staticmethod
    def get_test_resource_path(path: str) -> str:
        """
        获取Resources目录里的资源
        :param path: 需要获取的文件相对路径
        :return: 返回文件的绝对路径
        """
        root_path = ResourceUtil.get_root_path()
        return f"{root_path}/src/test/resources/{path}"

    @staticmethod
    def get_root_path() -> str:
        """
        获取项目根路径
        :return: 根目录
        """
        return os.getcwd().split(PROJECT_NAME)[0] + f"{PROJECT_NAME}"
