from src.main.code.dto.HandlerDto import HandlerDto


class NoEleHandlerDto(HandlerDto):
    """
    不需要查找元素的dto
    """

    __slots__ = ("__waitTime", "__ext")

    def __init__(self):
        # 等待的时间
        self.__waitTime = None
        # 扩展字段,具体用法见对应的handler描述
        self.__ext = None

    @property
    def wait_time(self):
        return self.__waitTime

    @wait_time.setter
    def wait_time(self, value):
        self.__waitTime = value

    @property
    def ext(self):
        return self.__ext

    @ext.setter
    def ext(self, value):
        self.__ext = value

    def to_dict(self):
        return {
            "waitTime": self.__waitTime,
            "ext": self.__ext,
        }
