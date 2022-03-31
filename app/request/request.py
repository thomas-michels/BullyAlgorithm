"""
    Module for request
"""
from app.process import Process


class Request:
    """
    Request class
    """

    @staticmethod
    def send(sender: Process, receiver: Process) -> bool:
        """
        Method to send request

        :param:
            sender: Process
            receiver: Process

        :return:
            bool
        """
        try:
            if sender.is_active():
                return receiver.is_active()

            return False

        except Exception:
            return False
