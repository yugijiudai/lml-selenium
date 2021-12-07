from unittest import TestCase

from src.main.code.util.ReflectUtil import ReflectUtil


class TestDbUtil(TestCase):

    def test_reflect(self):
        param = {'className': 'GlobalConfig', 'model': 'src.main.code.config.GlobalConfig', 'methodName': 'test_hi', 'args': ['名字', '呵呵']}
        ReflectUtil.run_clz_method(**param)
        print(ReflectUtil.run_clz_method(className='GlobalConfig', model='src.main.code.config.GlobalConfig', methodName='test_me', args=[]))
