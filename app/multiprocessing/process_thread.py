"""
    Module for Threads
"""
from threading import Thread
from time import sleep


class ProcessThread(Thread):
    """
    Process Thread class
    """
    def __init__(self, time_await, function):
        Thread.__init__(self)
        self.time_await = time_await
        self.function = function

    def run(self):
        while True:
            sleep(self.time_await)
            self.function()
