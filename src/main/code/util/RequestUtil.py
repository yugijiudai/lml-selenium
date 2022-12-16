# @Author:lml
# @Time:2022/1/8 1:19
# @File     :RequestUtil.py
import gzip
import re
from io import BytesIO

from src.main.code.dto.RequestDto import RequestDto
from src.main.code.util.InitUtil import InitUtil
from src.main.code.util.JsUtil import JsUtil
from src.main.code.util.JsonUtil import JsonUtil


class RequestUtil:

    @classmethod
    def capture_request(cls):
        """
        对请求捉包,并且获取到对应的request和response
        """
        JsUtil.wait_page_load()
        driver = InitUtil.get_driver()
        request_result = []
        for request in driver.requests:
            if cls.is_static_resource(request.url) or 'json' not in request.headers['accept']:
                continue
            request_dto = RequestDto()
            request_dto.url = request.path
            request_dto.method = request.method
            request_dto.response = cls.decode_json(request.response.body)
            request_dto.request_header = dict(request.headers)
            request_dto.response_header = dict(request.response.headers)
            if request.method == 'POST':
                request_dto.param = cls.decode_json(request.body)
            elif request.method == 'GET':
                request_dto.param = request.params
            # print(JsonUtil.to_json_str(request_dto.to_dict()))
            request_result.append(request_dto)
        return request_result

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

    @staticmethod
    def decode(val) -> str:
        """
        对对应的值进行解码
        :param val: 要解码的值
        :return: 返回解码后的值
        """
        try:
            return val.decode()
        except Exception:
            buff = BytesIO(val)
            f = gzip.GzipFile(fileobj=buff)
            return f.read().decode('utf-8')

    @classmethod
    def decode_json(cls, val) -> str:
        """
        对对应的值进行解码
        :param val: 要解码的值
        :return: 返回解码后的值
        """
        result = cls.decode(val)
        if JsonUtil.is_json(result):
            # 这里要转两次才能让结果输出到一行且没有各种\n的符号
            return JsonUtil.str_to_json(result)
        return result
