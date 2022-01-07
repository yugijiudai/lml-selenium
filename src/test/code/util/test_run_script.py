# @Author:lml
# @Time:2022/1/7 23:45
# @File     :test_run_script.py
from unittest import TestCase

import ddt

from src.main.code.dto.SeleniumDto import SeleniumDto
from src.main.code.enums.ActionEnum import ActionEnum
from src.main.code.handler.HandlerClient import HandlerClient
from src.main.code.util.EnumUtil import EnumUtil
from src.main.code.util.InitUtil import InitUtil

scripts_list = [
    {
        'script': 'function getTest(word){return word} return getTest(arguments[0])',
        'args': '有参数的js',
        'callFn': {'className': 'TestReflectUtil', 'model': 'src.test.code.util.test_reflect_util', 'methodName': 'test_hello'}
    },
    {
        'script': 'function getTest(word){return word} return getTest("无参数传递的js")',
        'callFn': {'className': 'TestReflectUtil', 'model': 'src.test.code.util.test_reflect_util', 'methodName': 'test_hello'}
    },
    {
        'script': 'function getTest(word){return word} getTest("js没有返回参数")',
        'callFn': {'className': 'TestReflectUtil', 'model': 'src.test.code.util.test_reflect_util', 'methodName': 'test_hello', 'args': ['js没有返回参数']}
    },
    {
        'script': 'function getTest(word){return word} getTest("没有回调方法")'
    }
]


@ddt.ddt
class TestRunScript(TestCase):

    @ddt.data(*scripts_list)
    def test_ddt(self, data):
        dto = SeleniumDto()
        dto.element_action = EnumUtil.get_enum_name(ActionEnum.RUN_SCRIPT)
        dto.ext = data
        HandlerClient.do_action(dto)

    def tearDown(self):
        InitUtil.close_driver()

    def setUp(self) -> None:
        InitUtil.init_all()
