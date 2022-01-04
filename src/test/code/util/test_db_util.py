from unittest import TestCase

from src.main.code.handler.HandlerClient import HandlerClient
# from src.main.code.handler.other.NoElementHandler import NoElementHandler
from src.main.code.handler.other.NoElementHandler import NoElementHandler
from src.main.code.util.DbUtil import DbUtil
from src.main.code.util.InitUtil import InitUtil
from src.main.code.util.ReflectUtil import ReflectUtil


class TestDbUtil(TestCase):

    def test_query(self):
        conn = DbUtil.get_conn()
        result = DbUtil.query_list(conn, 'select model as ext_val from explore_now where model = %s', ('登录'))
        for row in result:
            print(row)
        DbUtil.close_conn(conn)

    def test_load_test_case(self):
        selenium_dto_list = InitUtil.load_test_case("百度")
        for item in selenium_dto_list:
            HandlerClient.do_action(item)

    def test_child(self):
        # print(ReflectUtil.get_sub2(ElementHandler))
        print(ReflectUtil.get_sub(NoElementHandler, ['src.main.code.handler.element', 'src.main.code.handler.other']))
        # print(ReflectUtil.get_sub(NoElementHandler, 'src.main.code.handler.other'))
        # module = importlib.import_module(NoElementHandler.__module__)
        # for name, sub_class in inspect.getmembers(module):
        #     if inspect.isclass(sub_class):  # 类别是class，并且父类是A
        #             print(sub_class.__name__)
        # print(m)
        # print(m.__file__)
        # print(m.__class__.__name__)
        # print([cls.__name__ for cls in NoElementHandler.__subclasses__()])
        # print(ReflectUtil.get_sub(NoElementHandler))
        # print(ReflectUtil.get_all_subclasses(NoElementHandler()))

    # def get_verbose_prefix(self, o):
    #     """Returns an informative prefix for verbose debug output messages"""
    #     klass = o.__class__
    #     module = klass.__module__
    #     if module == 'builtins':
    #         return klass.__qualname__ # avoid outputs like 'builtins.str'
    #     return module + '.' + klass.__qualname__
