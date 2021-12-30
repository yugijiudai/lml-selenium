# Author : lml
# Date : 2021/12/28

"""
文件说明
"""
from src.main.code.enums.ActionEnum import ActionEnum
from src.main.code.handler.other.NoElementHandler import NoElementHandler
from src.main.code.util.JsonUtil import JsonUtil
from src.main.code.util.ReflectUtil import ReflectUtil


class RunMethodHandler(NoElementHandler):
    """
    执行自定义方法的处理器
    """

    def get_action(self) -> ActionEnum:
        return ActionEnum.runMethod

    def do_handle(self, handle_dto) -> None:
        """
        ext的格式如下:
        {
            'className': 'GlobalConfig', 类名
            'model': 'src.main.code.config.GlobalConfig', 对应的py文件全路径
            'methodName': 'test_hi', 需要调用的方法名
            'args': ['名字', '呵呵'] 这个方法需要用到的参数
        }
        """
        ext = handle_dto.ext
        run_method_obj = JsonUtil.str_to_json(ext)
        ReflectUtil.run_clz_method(**run_method_obj)

    def pre_handle(self, handle_dto) -> bool:
        return True
