# @Author:lml
# @Time:2021/12/8 0:25
# @File     :ReflectUtil.py
import importlib
import inspect


class ReflectUtil:
    """
    反射工具类
    """

    @classmethod
    def run_clz_method(cls, **config):
        """
        利用放射点用类里面的方法
        :param config: 调用这个方法需要提供方法名字,模块名字,类名字,参数名字
        :return:
        """
        class_name = config['className']
        func_param = config['args']
        model = importlib.import_module(config['model'])
        clz = getattr(model, class_name)
        method_name = config['methodName']
        func = getattr(clz, method_name)
        decorators = cls.get_decorators(func)
        if 'classmethod' in decorators or 'staticmethod' in decorators:
            # 实例方法和类方法直接调用,无需实例化类对象导致内存浪费
            return func(*func_param)
        return getattr(clz(), method_name)(*func_param)

    @classmethod
    def get_decorators(cls, function) -> list:
        """
        获取方法上装饰器的东西
        :param function: 要获取的方法
        :return: 返回装饰器的列表
        """
        source = inspect.getsource(function)
        index = source.find("def ")
        return [
            # line.strip().split()[0]
            line.strip().split()[0][1:]
            for line in source[:index].strip().splitlines()
            if line.strip()[0] == "@"
        ]
