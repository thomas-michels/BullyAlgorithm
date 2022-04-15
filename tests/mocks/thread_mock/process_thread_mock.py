"""
    Module for ProcessThreadMock
"""


class ProcessThreadMock:
    """
    Mock for ProcessThread
    """

    def __init__(self, time, function) -> None:
        self.time = time
        self.function = function

    def start(self):
        """
        Method to simulate thread is started
        """

    def join(self):
        """
        Method to simulate thread join
        """
