# Author : lml
# Date : 2021/12/6

import json5

from src.main.code.util.ResourceUtil import ResourceUtil


class InitUtil:
    """
    初始化的工具类
    """

    @staticmethod
    def init_setting():
        with open(ResourceUtil.get_resource_path('seleniumSetting.json5'), 'r', encoding='UTF-8') as load_f:
            return json5.load(load_f)
