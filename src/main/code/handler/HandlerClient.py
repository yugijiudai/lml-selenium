# Author : lml
# Date : 2021/12/30
from src.main.code.dto.selenium_dto import SeleniumDto
from src.main.code.enums.ActionEnum import ActionEnum


class HandlerClient:
    """
    文件说明
    """

    @staticmethod
    def do_action(selenium_dto: SeleniumDto):
        # element_action = selenium_dto.element_action
        # action_enum = ActionEnum[element_action]
        print(selenium_dto.element_action == ActionEnum.CLICK.name)
        # print(ActionEnum[str(selenium_dto.element_action)])
        # print(selenium_dto.element_action)
