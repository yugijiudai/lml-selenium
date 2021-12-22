from unittest import TestCase

from src.main.code.util.ClassGeneratorUtil import ClassGeneratorUtil
from src.main.code.util.ReflectUtil import ReflectUtil
from src.main.code.util.ResourceUtil import ResourceUtil


class TestReflectUtil(TestCase):

    def test_reflect(self):
        param = {'className': 'GlobalConfig', 'model': 'src.main.code.config.GlobalConfig', 'methodName': 'test_hi', 'args': ['名字', '呵呵']}
        ReflectUtil.run_clz_method(**param)
        print(ReflectUtil.run_clz_method(className='GlobalConfig', model='src.main.code.config.GlobalConfig', methodName='test_clz', args=[]))
        print(ReflectUtil.run_clz_method(className='GlobalConfig', model='src.main.code.config.GlobalConfig', methodName='get_config', args=[]))

    def test_gen_cls(self):
        ClassGeneratorUtil.generate_cls("HandleDto", f'{ResourceUtil.get_root_path()}/src/main/code/dto/HandleDto.py',
                                        params=["element", "by", "clickActionEnum", "keys"])
