from unittest import TestCase

import json5
import ujson

from src.main.code.util.JsonUtil import JsonUtil
from src.main.code.util.ResourceUtil import ResourceUtil


class TestJsonUtil(TestCase):

    def test_load(self):
        with open(ResourceUtil.get_resource_path('testJson.json5'), 'r', encoding='UTF-8') as load_f:
            content = json5.load(load_f)
            print(JsonUtil.to_json_str(content))

    def test_script(self):
        with open(ResourceUtil.get_resource_path('testJson.json5'), 'r', encoding='UTF-8') as load_f:
            result = JsonUtil.load_json5(load_f)
            # content = ujson.loads(load_f)
            print(ujson.dumps(result, ensure_ascii=False,))
            # print(JsonUtil.to_json_str(content))