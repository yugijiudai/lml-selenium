# @Author:lml
# @Time:2021/12/7 22:19
# @File     :DbUtil.py

import pymysql


class DbUtil:
    """
    数据库工具类
    """

    @classmethod
    def get_conn(cls):
        """
        获取数据库连接
        :return: 数据库的连接
        """
        return pymysql.connect(host='localhost', user='root', password='111111', database='selenium', port=3306)

    @classmethod
    def query_list(cls, connection, sql, *arr) -> list:
        """
        根据sql查询结果集
        :param connection: 数据库连接
        :param sql: 查询的sql
        :param arr: 查询的参数
        :return: 拼装好的list(dict)
        """
        cur = connection.cursor()
        cur.execute(sql, *arr)
        all_result = cur.fetchall()
        cols = cur.description
        col_len = len(cols)
        result_list = []
        for row in all_result:
            value = dict()
            for index in range(col_len):
                value[cols[index][0]] = row[index]
            result_list.append(value)
        return result_list

    @staticmethod
    def close_conn(con) -> None:
        """
        关闭连接
        :param con: 当前的连接
        """
        con.close()
