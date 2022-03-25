"""
    Module for request
"""
from app.process import Process
from app.exceptions import SenderOffline


class Request:
    """
    Request class
    """

    @classmethod
    def send(sender: Process, receiver: Process) -> bool:
        """
        Method to send request

        :param:
            sender: Process
            receiver: Process

        :return:
            bool
        """
        if sender.is_active:
            return receiver.is_active

        raise SenderOffline()
