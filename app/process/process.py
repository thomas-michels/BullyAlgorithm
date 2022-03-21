"""
Process module
"""

from typing import NoReturn
from app.utils import GenerateID


class Process:

    __id: int
    __is_active: bool = True

    def __init__(self) -> None:
        self.__id = GenerateID().get_id()

    def get_id(self) -> int:
        """
        Method to get id of Process

        :return:
            int
        """
        return self.__id

    def change_status(self) -> NoReturn:
        """
        Method to change status of process

        :return:
            NoReturn
        """
        self.__is_active = not self.__is_active

    def is_active(self) -> bool:
        """
        Method to check if process is active

        :return:
            Bool
        """
        return self.__is_active

    def send_request(self, process) -> bool:
        """
        Method to send message for another process

        :param:
            process: Process

        :return:
            Bool
        """
        if self.is_active():
            return process.is_active()

        return False
