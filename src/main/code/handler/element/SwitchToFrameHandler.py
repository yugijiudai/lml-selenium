# Author : lml
# Date : 2021/12/17
from loguru import logger
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from src.main.code.config.GlobalConfig import GlobalConfig
from src.main.code.enums.ActionEnum import ActionEnum
from src.main.code.handler.element.ElementHandler import ElementHandler
from src.main.code.util.InitUtil import InitUtil


class SwitchToFrameHandler(ElementHandler):
    """
    切换frame处理器
    """

    def get_action(self) -> ActionEnum:
        return ActionEnum.SWITCH_TO_FRAME

    def do_handle(self, ele_handle_dto) -> None:
        element = ele_handle_dto.elements[0]
        by = ele_handle_dto.by
        WebDriverWait(InitUtil.get_driver(), GlobalConfig.get_config()['waitElement']).until(EC.frame_to_be_available_and_switch_to_it(element))
        logger.debug("使用{}切换[{}],frame成功", by, element)

    def pre_handle(self, ele_handle_dto) -> bool:
        return True
