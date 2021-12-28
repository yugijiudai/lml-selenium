# @Author:lml
# @Time:2021/12/6 22:07
# @File     :GlobalConfig.py

class GlobalConfig:
    """
    全局的配置文件
    """

    @staticmethod
    def get_config():
        """
        读取配置
        """
        return {
            # chromeDriver位置
            "driverPath": "/Volumes/common/dev/driver/chromedriver",
            # "driverPath": "D:\\driver\\chromedriver.exe",
            # 查找元素的重试次数
            "retry": 2,
            #  查找元素的时候等待元素的时间(显示等待,单位秒)
            "waitElement": 1,
            # 等待页面加载的最长时间(显示等待,单位秒)
            "pageLoad": 10,
            # 强制等待时间(单位秒)
            "waitTime": 0.5,
            # 是否打开浏览器
            "useNoHead": True
        }

    def test_hi(self, name, hi):
        print(name)
        print(hi)

    def test_me(self):
        return 'hi'

    @classmethod
    def test_clz(cls):
        return '类方法'
