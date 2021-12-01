# Author : lml
# Date : 2021/12/1
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from seleniumwire import webdriver


class SeleniumUtil:
    """
    selenium工具类
    """

    selenium_driver = None

    @classmethod
    def get_driver(cls):
        """
        初始化selenium的驱动并且返回
        :return: 初始化好的驱动
        """
        options = webdriver.ChromeOptions()
        # options.add_argument('User-Agent=Mozilla/5.0 (Linux; U; Android 8.1.0; zh-cn; BLA-AL00 Build/HUAWEIBLA-AL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.132 MQQBrowser/8.9 Mobile Safari/537.36')
        # 浏览器不提供可视化页面
        # options.add_argument('--headless')
        # 禁用扩展
        options.add_argument('disable-extensions')
        # 禁用阻止弹出窗口
        options.add_argument('--disable-popup-blocking')
        # 设置这两个参数就可以避免密码提示框的弹出
        options.add_experimental_option('prefs', {
            'credentials_enable_service': False,
            'profile.password_manager_enabled': False
        })
        cls.selenium_driver = webdriver.Chrome(chrome_options=options, executable_path='/Volumes/common/dev/driver/chromedriver')
        return cls.selenium_driver

    @staticmethod
    def get_request_msg(web_driver):
        for request in web_driver.requests:
            if request.response:
                print(request)

    @classmethod
    def close_driver(cls):
        """
        关闭driver
        """
        cls.selenium_driver.quit()

    @classmethod
    def find_element(cls, by, value) -> WebElement:
        return WebDriverWait(cls.selenium_driver, 10).until(lambda browser: browser.find_elements(by, value))


if __name__ == '__main__':
    driver = SeleniumUtil.get_driver()
    driver.get('https://www.baidu.com')
    # element = WebDriverWait(driver, 10).until(lambda browser: browser.find_elements(By.ID, 'kw'))
    elements = SeleniumUtil.find_element(By.ID, 'kw')
    elements[0].send_keys('selenium')
    SeleniumUtil.close_driver()
