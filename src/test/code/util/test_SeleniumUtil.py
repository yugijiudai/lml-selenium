# Author : lml
# Date : 2021/12/6

from unittest import TestCase

from selenium.webdriver.common.by import By

from src.main.code.util.SeleniumUtil import SeleniumUtil


class TestSeleniumUtil(TestCase):

    def test_get_driver(self):
        driver = SeleniumUtil.get_driver()
        driver.get('https://www.baidu.com')
        SeleniumUtil.send_keys(By.ID, "kw", 'selenium')
        SeleniumUtil.click_ele(by=By.ID, path='su')

    def tearDown(self):
        SeleniumUtil.close_driver()
