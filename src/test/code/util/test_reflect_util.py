from unittest import TestCase

from src.main.code.util.ClassGeneratorUtil import ClassGeneratorUtil
from src.main.code.util.ReflectUtil import ReflectUtil
from src.main.code.util.ResourceUtil import ResourceUtil


class TestReflectUtil(TestCase):

    def test_reflect(self):
        param = {'className': 'TestReflectUtil', 'model': 'src.test.code.util.test_reflect_util', 'methodName': 'test_hi', 'args': ['名字', '呵呵']}
        ReflectUtil.run_clz_method(**param)
        print(ReflectUtil.run_clz_method(className='TestReflectUtil', model='src.test.code.util.test_reflect_util', methodName='test_clz', args=[]))
        print(ReflectUtil.run_clz_method(className='TestReflectUtil', model='src.test.code.util.test_reflect_util', methodName='test_static', args=[]))

    def test_gen_cls(self):
        ClassGeneratorUtil.generate_cls("SeleniumDto", f'{ResourceUtil.get_root_path()}/src/main/code/dto/selenium_dto.py',
                                        params=["id", "description", "model", "element_action", "element", "find_type", "script", "wait",
                                                "retry", "click_action", "valid", "ext", "call_back"])

    def test_hi(self, name, hi):
        print(name)
        print(hi)

    def test_hello(self, name):
        print(name)

    def test_me(self):
        return 'hi'

    @classmethod
    def test_clz(cls):
        return '类方法'

    @staticmethod
    def test_static():
        return '静态方法'
