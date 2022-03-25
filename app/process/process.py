"""
Process module
"""

from app.utils import GenerateID


class Process:

    def __init__(self) -> None:
        self.__id = GenerateID().get_id()
        self.__is_active = True

    def get_id(self) -> int:
        """
        Method to get id of Process

        :return:
            int
        """
        return self.__id

    def change_status(self) -> None:
        """
        Method to change status of process

        :return:
            None
        """
        self.__is_active = not self.__is_active

    def is_active(self) -> bool:
        """
        Method to check if process is active

        :return:
            Bool
        """
        return self.__is_active
