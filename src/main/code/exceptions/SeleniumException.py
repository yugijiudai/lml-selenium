# @Author:lml
# @Time:2022/1/8 0:14
# @File     :SeleniumException.py


class SeleniumException(Exception):
    """
    selenium的相关异常
    """

    def __init__(self, msg):
        self.msg = msg
        Exception.__init__(self, msg)

    def __str__(self):
        return self.msg
