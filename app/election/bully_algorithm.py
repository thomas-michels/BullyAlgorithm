"""
Bully Algorithm module
"""
from app.election.election import ElectionInterface
from app.process import Process
from typing import List

from app.request.request import Request


class BullyAlgorithm(ElectionInterface):
    """
    Bully Algorithm Class
    """

    def __init__(self) -> None:
        super().__init__()

    def run_election(self, process_start: Process, processes: List[Process]) -> Process:
        """
        Method to run new election and return new coordenator

        :param:
            process_start: Process
            processes: List[Process]

        :return:
            Process
        """
        print(f"Eleição iniciada pelo processo com o ID {process_start.get_id()}")

        higher_process = process_start
        for process in processes:
            print(f"Enviado mensagem para o processo com o ID {process.get_id()}")
            print(f"Mensagem {'Aceita' if Request.send(sender=process_start, receiver=process) else 'Negada'}")

            if process.get_id() > higher_process.get_id() and process.is_active():
                higher_process = process

        print(f"O coordenador selecionado foi o processo com o ID {higher_process.get_id()}")

        return higher_process
