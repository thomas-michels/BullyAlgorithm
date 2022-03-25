"""
GenerateID module
"""

from app.utils.singleton import Singleton


class GenerateID(Singleton):
    """
    Class to generate ID
    """

    __id: int = 0

    def get_id(self) -> int:
        self.__increment()
        return self.__id

    def __increment(self) -> None:
        """
        Autoincrement to id

        :return:
            None
        """

        self.__id += 1
