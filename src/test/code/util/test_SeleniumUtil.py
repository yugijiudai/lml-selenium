# Author : lml
# Date : 2021/12/6

from unittest import TestCase

from selenium.webdriver.common.by import By

from src.main.code.util.JsUtil import JsUtil
from src.main.code.util.SeleniumUtil import SeleniumUtil


class TestSeleniumUtil(TestCase):

    def test_get_driver(self):
        driver = SeleniumUtil.get_driver()
        driver.get('https://www.baidu.com')
        JsUtil.run_js('alert(111)')
        SeleniumUtil.click_alert()
        SeleniumUtil.send_keys(By.ID, "kw", 'selenium')
        SeleniumUtil.refresh()
        SeleniumUtil.send_keys(By.ID, "kw", 'selenium')
        find = SeleniumUtil.find_element(By.ID, 'su')
        JsUtil.run_js_with_param('arguments[0].click(); return 111', find)
        JsUtil.wait_page_load()
        SeleniumUtil.click_ele(by=By.ID, path='su')

    def tearDown(self):
        SeleniumUtil.close_driver()
