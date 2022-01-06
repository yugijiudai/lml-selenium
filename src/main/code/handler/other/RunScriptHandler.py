# Author : lml
# Date : 2021/12/30
from src.main.code.dto.NoEleHandlerDto import NoEleHandlerDto
from src.main.code.enums.ActionEnum import ActionEnum
from src.main.code.handler.other.NoElementHandler import NoElementHandler
from src.main.code.handler.other.RunMethodHandler import RunMethodHandler
from src.main.code.util.JsUtil import JsUtil


class RunScriptHandler(NoElementHandler):
    """
    执行脚本的处理器
    """

    def get_action(self) -> ActionEnum:
        return ActionEnum.RUN_SCRIPT

    def do_handle(self, handle_dto) -> None:
        """
        ext的格式如下:
        {
            'args': '123', js运行所需要的参数，非必填
            'script': 'console.log(111)', 要运行的js脚本
            'callFn': {} js运行完要执行的回调方法,可以把js的返回值作为参数带给这个回调方法, 格式和RunMethodHandler的ext一样
        }
        """
        ext = handle_dto.ext
        args = ext.get('args')
        call_fn = ext.get('callFn')
        script = ext['script']
        js_result = JsUtil.run_js(script) if args is None else JsUtil.run_js_with_param(script, args)
        if call_fn is not None:
            run_method_handler = RunMethodHandler()
            call_fn_args = call_fn['args'] if call_fn.get('args') is not None else []
            if js_result is not None:
                # 如果js脚本有返回参数,会把js的返回的结果append到回调方法的入参里面
                call_fn_args.append(js_result)
            # 把js脚本的结果作为回调方法的入参
            call_fn['args'] = call_fn_args
            no_ele_handle_dto = NoEleHandlerDto()
            no_ele_handle_dto.ext = call_fn
            run_method_handler.do_handle(no_ele_handle_dto)

    def pre_handle(self, handle_dto) -> bool:
        return True
