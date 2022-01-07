# @Author:lml
# @Time:2022/1/8 1:19
# @File     :RequestUtil.py
import re

from src.main.code.util.InitUtil import InitUtil
from src.main.code.util.JsUtil import JsUtil


class RequestUtil:

    @classmethod
    def capture_request(cls):
        """
        对请求捉包,并且获取到对应的request和response
        """
        JsUtil.wait_page_load()
        driver = InitUtil.get_driver()
        for request in driver.requests:
            if cls.is_static_resource(request.url) or 'json' not in request.headers['accept']:
                continue
            if request.method == 'POST':
                print(f'post请求: {request.body.decode()}')
            elif request.method == 'GET':
                print(f'get请求: {request.params}')
        print("打印完成....")

    @classmethod
    def is_static_resource(cls, url: str) -> bool:
        """
        判断是否静态资源
        :param url: 要校验的url
        :return: true表示是
        """
        if url.startswith('http') is False:
            return True
        return re.search('.*(css|ico|jpg|jpeg|png|gif|bmp|wav|js|woff2|woff|json|svg)(\\?.*)?$', url) is not None
