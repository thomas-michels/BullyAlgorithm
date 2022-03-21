"""
Election interface module
"""

from abc import ABC
from typing import List
from app.process import Process


class ElectionInterface(ABC):
    """
    Election Interface class
    """

    def run_election(self, process_start: Process, processes: List[Process]) -> Process:
        """
        Method to run new election and return new coordenator

        :param:
            process_start: Process
            processes: List[Process]

        :return:
            Process
        """
