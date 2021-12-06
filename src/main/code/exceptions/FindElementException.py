# Author : lml
# Date : 2021/12/6


class FindElementException(Exception):
    """
    查找元素的异常
    """

    def __init__(self, msg):
        self.msg = msg
        Exception.__init__(self, msg)

    def __str__(self):
        return self.msg
