# @Author:lml
# @Time:2022/1/8 0:05
# @File     :BaseSeleniumTest.py


import abc
from unittest import TestCase

from src.main.code.config.Logger import MyLogger
from src.main.code.exceptions.SeleniumException import SeleniumException
from src.main.code.handler.HandlerClient import HandlerClient
from src.main.code.util.InitUtil import InitUtil


class BaseSeleniumTest(TestCase):
    """
    selenium测试基础类
    """

    @abc.abstractmethod
    def get_case(self) -> str:
        """
        抽象方法,需要子类继承这个来给出对应的表名
        :return: 返回用例的表名
        """
        pass

    def do_test(self, model: str) -> None:
        """
        根据提供的模块来执行对应模块的测试用例
        :param model: 模块的名字
        """
        case_name = self.get_case()
        selenium_dto_list = InitUtil.load_test_case(case_name, model)
        for item in selenium_dto_list:
            try:
                HandlerClient.do_action(item)
            except Exception:
                msg = f'执行用例:【{case_name}】模块【{model}】步骤【{item.id}】时出错'
                MyLogger.log_error(msg)
                raise SeleniumException(msg)

    def tearDown(self):
        InitUtil.close_driver()

    def setUp(self) -> None:
        InitUtil.init_all()
