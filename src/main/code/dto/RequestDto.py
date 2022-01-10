class RequestDto:
    __slots__ = ('__url', '__param', '__response', '__request_header', '__method', '__response_header')

    def __init__(self):
        self.__url = None
        self.__param = None
        self.__response = None
        self.__request_header = None
        self.__method = None
        self.__response_header = None

    @property
    def url(self):
        return self.__url

    @url.setter
    def url(self, value):
        self.__url = value

    @property
    def param(self):
        return self.__param

    @param.setter
    def param(self, value):
        self.__param = value

    @property
    def response(self):
        return self.__response

    @response.setter
    def response(self, value):
        self.__response = value

    @property
    def request_header(self):
        return self.__request_header

    @request_header.setter
    def request_header(self, value):
        self.__request_header = value

    @property
    def method(self):
        return self.__method

    @method.setter
    def method(self, value):
        self.__method = value

    @property
    def response_header(self):
        return self.__response_header

    @response_header.setter
    def response_header(self, value):
        self.__response_header = value

    def to_dict(self):
        return {
            "url": self.__url,
            "param": self.__param,
            "response": self.__response,
            "request_header": self.__request_header,
            "method": self.__method,
            "response_header": self.__response_header,
        }
