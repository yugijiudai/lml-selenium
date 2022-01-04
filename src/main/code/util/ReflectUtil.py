# @Author:lml
# @Time:2021/12/8 0:25
# @File     :ReflectUtil.py
import importlib
import inspect
import os

from src.main.code.exceptions.InitException import InitException
from src.main.code.util.ResourceUtil import ResourceUtil


class ReflectUtil:
    """
    反射工具类
    """

    def __init__(self) -> None:
        raise InitException("该类不允许初始化")

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
            # 如果包含@字符串就把他们全部拿出来拼接成一个list并且返回
            line.strip().split()[0][1:] for line in source[:index].strip().splitlines() if line.strip()[0] == "@"
        ]

    @classmethod
    def get_sub(cls, father, packages) -> set:
        """
        根据给定的父类和指定的包名，获取这个包名下是这个父类的所有子类，只能获取直属一级的子类
        :param father: 父类
        :param packages: 要获取的包
        :return: 返回一个子类set
        """
        sub_clz_list = set()
        for package in packages:
            current_files = set()
            current_path = f"{ResourceUtil.get_root_path()}/{package.replace('.', '/')}"
            for root, dirs, files in os.walk(current_path):
                # 获取这个路径下不包含__init__.py的文件
                current_files.update({file.split('.py')[0] for file in files if file != '__init__.py'})
            for f in current_files:
                module = importlib.import_module('.%s' % f, package=package)
                for name, sub_class in inspect.getmembers(module):
                    if inspect.isclass(sub_class) and sub_class.__base__ == father:
                        obj_class_name = getattr(module, sub_class.__name__)
                        # 根据子类名称从m.py中获取该类
                        sub_clz_list.add(obj_class_name)
        return sub_clz_list
