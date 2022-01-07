# Author : lml
# Date : 2021/12/6

from selenium.webdriver.common.by import By

from src.main.code.dto.SeleniumDto import SeleniumDto
from src.main.code.enums.ActionEnum import ActionEnum
from src.main.code.handler.HandlerClient import HandlerClient
from src.main.code.util.EnumUtil import EnumUtil
from src.main.code.util.JsUtil import JsUtil
from src.main.code.util.RequestUtil import RequestUtil
from src.main.code.util.SeleniumUtil import SeleniumUtil
from src.test.code.BaseSeleniumTest import BaseSeleniumTest


class TestSeleniumUtil(BaseSeleniumTest):

    def test_run_method(self):
        """
        测试runMethod和runScript的各种情景
        """
        dto = SeleniumDto()
        dto.element_action = EnumUtil.get_enum_name(ActionEnum.RUN_METHOD)
        param = {'className': 'TestReflectUtil', 'model': 'src.test.code.util.test_reflect_util', 'methodName': 'test_hi', 'args': ['名字', '呵呵']}
        dto.ext = param
        HandlerClient.do_action(dto)

    def test_selenium_util(self):
        """
        使用seleniumUtil直接执行的方法
        """
        SeleniumUtil.get_url('https://www.baidu.com')
        JsUtil.run_js('alert(111)')
        SeleniumUtil.click_alert()
        SeleniumUtil.send_keys(By.ID, "kw", 'selenium')
        SeleniumUtil.refresh()
        SeleniumUtil.send_keys(By.ID, "kw", 'selenium')
        find = SeleniumUtil.find_element(By.ID, 'su')
        print(JsUtil.run_js_with_param('arguments[0].click(); return 111', find))
        JsUtil.wait_page_load()
        SeleniumUtil.click_ele(by=By.ID, path='su')

    def get_case(self) -> str:
        return "demo_py"

    def test_load_test_case2(self):
        SeleniumUtil.get_url('https://www.baidu.com')
        super().do_test("百度")
        JsUtil.wait_page_load()
        # SeleniumUtil.get_request_msg()

    def test_radar(self):
        SeleniumUtil.get_url('')
        SeleniumUtil.send_keys(By.CSS_SELECTOR,
                               "div.lego-base-framework:nth-child(2) div.lego-container__lego-login:nth-child(2) div.bnr-login.brandradar-beauty-matrix-datastory-com-cn.bnr__light.is-dynamic-bg div.bnr-login-page div.bnr-login-page__container div.bnr-login-page__form-item:nth-child(1) > input.bnr-login-page__form-input",
                               "")
        SeleniumUtil.send_keys(By.CSS_SELECTOR,
                               "div.lego-base-framework:nth-child(2) div.lego-container__lego-login:nth-child(2) div.bnr-login.brandradar-beauty-matrix-datastory-com-cn.bnr__light.is-dynamic-bg div.bnr-login-page div.bnr-login-page__container div.bnr-login-page__form-item:nth-child(2) > input.bnr-login-page__form-input",
                               "")
        SeleniumUtil.click_ele(By.CSS_SELECTOR,
                               "div.lego-base-framework:nth-child(2) div.lego-container__lego-login:nth-child(2) div.bnr-login.brandradar-beauty-matrix-datastory-com-cn.bnr__light.is-dynamic-bg div.bnr-login-page div.bnr-login-page__container > button.el-button.bnr-login-page__login-btn.el-button--default:nth-child(4)")
        JsUtil.wait_page_load()
        SeleniumUtil.click_ele(By.CSS_SELECTOR, "div[title='品牌监测']")
        JsUtil.wait_page_load()
        RequestUtil.capture_request()
