"""
GenerateID module
"""

from typing import NoReturn
from app.utils.singleton import Singleton


class GenerateID(Singleton):
    """
    Class to generate ID
    """

    __id: int = 0

    def get_id(self) -> int:
        self.__increment()
        return self.__id

    def __increment(self) -> NoReturn:
        """
        Autoincrement to id

        :return:
            NoReturn
        """

        self.__id += 1
