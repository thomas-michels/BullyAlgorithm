"""
    Module for Process Manager class
"""

from typing import List, NoReturn
from random import choice
from app.request import Request
from app.coordenator import Coordenator
from app.process import Process
from app.election import ElectionInterface


class ProcessManager:
    """
    ProcessManager class
    """

    __processes: List[Process] = []
    __coordenator: Coordenator = None
    __election_type: ElectionInterface

    def __init__(self, election_algotithm: ElectionInterface) -> None:
        self.__election_type = election_algotithm

    def get_processes(self) -> List[Process]:
        """
        Method for get all processess

        :return:
            List[Process]
        """
        return self.__processes

    def new_process(self) -> NoReturn:
        """
        Method to create new process

        :return:
            NoReturn
        """
        process = Process()
        self.__processes.append(process)
        print(f"O Processo com o ID {process.get_id()} foi criado!")

    def deactive_process(self, process: Process) -> NoReturn:
        """
        Method to deactive process

        :param:
            process: Process

        :return:
            NoReturn
        """
        process.change_status()
        print(f"O processo com o ID {process.get_id()} foi desativado!")

    def set_coordenator(self, process: Process) -> NoReturn:
        """
        Method to set new coordenator

        :return:
            NoReturn
        """
        self.__coordenator = Coordenator(process=process)

    def get_coordenator(self) -> Coordenator:
        """
        Method to get coordenator of processes

        :return:
            Coordenator
        """
        self.__coordenator

    def election_time(self) -> NoReturn:
        """
        Method to run election of coordenator

        :return:
            NoReturn
        """
        process = choice(self.get_processes())
        if Request.send(self.__coordenator):
            self.__election_type.run_election(process_start=process, processes=self.get_processes())
