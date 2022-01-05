# Author : lml
# Date : 2021/12/6

from unittest import TestCase

from selenium.webdriver.common.by import By

from src.main.code.enums.ClickActionEnum import ClickActionEnum
from src.main.code.handler.HandlerClient import HandlerClient
from src.main.code.handler.element.ClickHandler import ClickHandler
from src.main.code.handler.element.SendKeyHandler import SendKeyHandler
from src.main.code.handler.other.AlertHandler import AlertHandler
from src.main.code.handler.other.RefreshHandler import RefreshHandler
from src.main.code.handler.other.RunMethodHandler import RunMethodHandler
from src.main.code.handler.other.RunScriptHandler import RunScriptHandler
from src.main.code.util.InitUtil import InitUtil
from src.main.code.util.JsUtil import JsUtil
from src.main.code.util.SeleniumUtil import SeleniumUtil


class TestSeleniumUtil(TestCase):

    def test_handler(self):
        InitUtil.init_all()
        SeleniumUtil.get_url('https://www.baidu.com')
        SeleniumUtil.retry_find_and_do(handler=RunScriptHandler(), ext={'script': 'alert(111)'})
        SeleniumUtil.retry_find_and_do(handler=AlertHandler())
        SeleniumUtil.retry_find_and_do(by=By.ID, path='kw', handler=SendKeyHandler(), keys="selenium")
        SeleniumUtil.retry_find_and_do(handler=RefreshHandler())
        SeleniumUtil.retry_find_and_do(by=By.ID, path='kw', handler=SendKeyHandler(), keys="selenium")
        SeleniumUtil.retry_find_and_do(by=By.ID, path='su', handler=ClickHandler(), clickActionEnum=ClickActionEnum.BY_TAG_TYPE)
        JsUtil.wait_page_load()

    def test_no_ele_handler(self):
        param = {'className': 'TestReflectUtil', 'model': 'src.test.code.util.test_reflect_util', 'methodName': 'test_hi', 'args': ['名字', '呵呵']}
        SeleniumUtil.retry_find_and_do(handler=RunMethodHandler(), ext=param)
        para_script = {
            'script': 'function getTest(word){return word} return getTest(arguments[0])',
            'args': '有参数的js',
            'callFn': {'className': 'TestReflectUtil', 'model': 'src.test.code.util.test_reflect_util', 'methodName': 'test_hello'}
        }
        SeleniumUtil.retry_find_and_do(handler=RunScriptHandler(), ext=para_script)
        no_para_script = {
            'script': 'function getTest(word){return word} return getTest("哈哈哈")',
            'callFn': {'className': 'TestReflectUtil', 'model': 'src.test.code.util.test_reflect_util', 'methodName': 'test_hello'}
        }
        SeleniumUtil.retry_find_and_do(handler=RunScriptHandler(), ext=no_para_script)
        no_return_script = {
            'script': 'function getTest(word){return word} getTest("js没有返回参数")',
            'callFn': {'className': 'TestReflectUtil', 'model': 'src.test.code.util.test_reflect_util', 'methodName': 'test_hello', 'args': ['js没有返回参数']}
        }
        SeleniumUtil.retry_find_and_do(handler=RunScriptHandler(), ext=no_return_script)
        no_call_fn_script = {
            'script': 'function getTest(word){return word} getTest("没有回调方法")'
        }
        SeleniumUtil.retry_find_and_do(handler=RunScriptHandler(), ext=no_call_fn_script)

    def test_selenium_util(self):
        """
        使用seleniumUtil直接执行的方法
        """
        InitUtil.init_all()
        SeleniumUtil.get_url('https://www.baidu.com')
        JsUtil.run_js('alert(111)')
        SeleniumUtil.click_alert()
        SeleniumUtil.send_keys(By.ID, "kw", 'selenium')
        SeleniumUtil.refresh()
        SeleniumUtil.send_keys(By.ID, "kw", 'selenium')
        find = SeleniumUtil.find_element(By.ID, 'su')
        JsUtil.run_js_with_param('arguments[0].click(); return 111', find)
        JsUtil.wait_page_load()
        SeleniumUtil.click_ele(by=By.ID, path='su')

    def test_load_test_case(self):
        InitUtil.init_all()
        SeleniumUtil.get_url('https://www.baidu.com')
        selenium_dto_list = InitUtil.load_test_case("百度")
        handler_client = HandlerClient()
        for item in selenium_dto_list:
            handler_client.do_action(item)
        JsUtil.wait_page_load()

    def tearDown(self):
        InitUtil.close_driver()

    def setUp(self) -> None:
        InitUtil.init_all()
