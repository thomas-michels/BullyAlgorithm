"""
    Module for Process Manager class
"""

from typing import List
from random import choice
from app.request import Request
from app.coordenator import Coordenator
from app.process import Process
from app.election import ElectionInterface


class ProcessManager:
    """
    ProcessManager class
    """

    def __init__(self, election_algotithm) -> None:
        self.__election_type: ElectionInterface = election_algotithm
        self.__processes: List[Process] = []
        self.__coordenator: Coordenator = None

    def get_active_processes(self) -> List[Process]:
        """
        Method for get all active processess

        :return:
            List[Process]
        """
        actives = []

        for process in self.__processes:
            if process.is_active():
                actives.append(process)

        return actives

    def new_process(self) -> None:
        """
        Method to create new process

        :return:
            None
        """
        process = Process()
        self.__processes.append(process)
        print(f"O Processo com o ID {process.get_id()} foi criado!")

    def deactive_random_process(self) -> None:
        """
        Method to deactive random process in processes list

        :return:
            None
        """
        chosen_process = choice(self.get_active_processes())
        self.deactive_process(chosen_process)

    def deactive_process(self, process: Process) -> None:
        """
        Method to deactive process

        :param:
            process: Process

        :return:
            None
        """
        process.change_status()
        print(f"O processo com o ID {process.get_id()} foi desativado!")

    def set_coordenator(self, process: Process) -> None:
        """
        Method to set new coordenator

        :return:
            None
        """
        self.__coordenator = Coordenator(process=process)

    def get_coordenator(self) -> Coordenator:
        """
        Method to get coordenator of processes

        :return:
            Coordenator
        """
        self.__coordenator

    def election_time(self) -> None:
        """
        Method to run election of coordenator

        :return:
            None
        """
        process = choice(self.get_active_processes())
        if process:
            if not Request.send(process, self.__coordenator):
                self.set_coordenator(self.__election_type.run_election(process_start=process, processes=self.get_active_processes()))
