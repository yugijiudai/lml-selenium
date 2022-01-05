from unittest import TestCase

from src.main.code.factory.HandlerFactory import HandlerFactory
from src.main.code.handler.HandlerClient import HandlerClient
# from src.main.code.handler.other.NoElementHandler import NoElementHandler
from src.main.code.util.DbUtil import DbUtil
from src.main.code.util.InitUtil import InitUtil
from src.main.code.util.StrUtil import StrUtil


class TestDbUtil(TestCase):

    def test_query(self):
        conn = DbUtil.get_conn()
        result = DbUtil.query_list(conn, 'select model as ext_val from explore_now where model = %s', ('登录'))
        for row in result:
            print(row)
        DbUtil.close_conn(conn)

    def test_load_test_case(self):
        HandlerFactory.init_all_handler()
        selenium_dto_list = InitUtil.load_test_case("百度")
        handler_client = HandlerClient()
        for item in selenium_dto_list:
            handler_client.do_action(item)

    def test_child(self):
        print(StrUtil.is_blank(''))
        print(StrUtil.is_blank(None))
        print(StrUtil.is_blank('fwefwe'))
