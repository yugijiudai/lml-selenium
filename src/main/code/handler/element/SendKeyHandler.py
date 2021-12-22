# Author : lml
# Date : 2021/12/17
from src.main.code.enums.ActionEnum import ActionEnum
from src.main.code.handler.SeleniumHandler import SeleniumHandler


class SendKeyHandler(SeleniumHandler):
    """
    输入框发送文本的处理器
    """

    def get_action(self) -> ActionEnum:
        return ActionEnum.sendKeys

    def do_handle(self, ele_handle_dto) -> None:
        element = ele_handle_dto.elements[0]
        # 先点中,然后清空,最后输入
        element.click()
        element.clear()
        element.send_keys(ele_handle_dto.keys)

    def pre_handle(self, ele_handle_dto) -> bool:
        return True

