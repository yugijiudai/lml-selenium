# Author : lml
# Date : 2021/12/28

from src.main.code.enums.ActionEnum import ActionEnum
from src.main.code.handler.other.NoElementHandler import NoElementHandler
from src.main.code.util.SeleniumUtil import SeleniumUtil


class RefreshHandler(NoElementHandler):
    """
    刷新页面处理器
    """

    def get_action(self) -> ActionEnum:
        return ActionEnum.refresh

    def do_handle(self, handle_dto) -> None:
        SeleniumUtil.refresh()

    def pre_handle(self, handle_dto) -> bool:
        return True
