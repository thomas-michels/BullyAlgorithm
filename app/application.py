"""
Application module
"""

from datetime import datetime
from threading import Timer
from typing import List, NoReturn
from random import choice
from app.process import Process
from app.election import ElectionInterface, BullyAlgorithm


class System:
    """ """

    __processes: List[Process] = []
    __coordenator: Process = None
    __election_type: ElectionInterface

    def __init__(self) -> None:
        self.__election_type = BullyAlgorithm()
        self.first_coordenator()
        self.run()

    def first_coordenator(self):
        self.new_process()
        self.set_coordenator(self.get_processes()[0])

    def get_processes(self) -> List[Process]:
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
        """ """
        self.__coordenator = process
        self.__processes.remove(process)

    def get_coordenator(self) -> Process:
        """ """
        self.__coordenator

    def election_time(self):
        process = choice(self.get_processes())
        if process.send_request(self.__coordenator):
            self.__election_type.run_election(process_start=process, processes=self.get_processes())

    def run(self):
        """ """

        print(f"Sistema Iniciado - {datetime.now()}")
        new_process = Timer(30, self.new_process())
        new_process.start()

        request_to_coordenator = Timer(
            25, self.election_time()
        )
        request_to_coordenator.start()

        inactive_coordenator = Timer(100, self.__coordenator.change_status())
        inactive_coordenator.start()

        inactive_process = Timer(80, choice(self.get_processes()).change_status())
        inactive_process.start()
