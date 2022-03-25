"""
    Module for Coordernator class
"""
from app.process import Process
from datetime import datetime


class Coordenator(Process):

    def __init__(self, process: Process) -> None:
        self.process = process
        self.active_time = datetime.now()
    
    def get_active_time(self) -> datetime:
        """
        Method to get active time of process

        :return:
            datetime
        """
        return self.__active_time
