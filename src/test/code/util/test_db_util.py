from unittest import TestCase

from src.main.code.handler.HandlerClient import HandlerClient
from src.main.code.util.DbUtil import DbUtil
from src.main.code.util.InitUtil import InitUtil


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
