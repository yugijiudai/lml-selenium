# @Author:lml
# @Time:2021/12/8 0:25
# @File     :ReflectUtil.py
import importlib


class ReflectUtil:
    """
    反射工具类
    """

    @staticmethod
    def run_clz_method(**config):
        """
        利用放射点用类里面的方法
        :param config: 调用这个方法需要提供方法名字,模块名字,类名字,参数名字
        :return:
        """
        func = config['methodName']
        class_name = config['className']
        func_param = config['args']
        model = importlib.import_module(config['model'])
        obj = getattr(model, class_name)()
        return getattr(obj, func)(*func_param)
