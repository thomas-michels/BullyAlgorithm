"""
    Module for election mock
"""

from app.election.election import ElectionInterface
from app.process import Process
from typing import List


class ElectionMock(ElectionInterface):
    """
    ElectionMock class    
    """

    def run_election(self, process_start: Process, processes: List[Process]) -> Process:
        print(f"Eleição iniciada pelo processo com o ID {process_start.get_id()}")
        print(f"O coordenador selecionado foi o processo com o ID {processes[0].get_id()}")
        return process_start
