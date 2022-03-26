"""
Application module
"""

from datetime import datetime
from app.process_manager import ProcessManager
from app.election import BullyAlgorithm
import sched, time


class Application:

    def __init__(self) -> None:
        self.process_manager = ProcessManager(BullyAlgorithm())
        self.scheduler = sched.scheduler(time.time, time.sleep)
        self.run()

    def run(self) -> None:
        """
        Method to run Application

        :return:
            None
        """
            
        self.schedules()

    def schedules(self):
        print(time.time())
        self.scheduler.enter(25, 1, self.process_manager.election_time())
        self.scheduler.enter(30, 1, self.process_manager.new_process())
        self.scheduler.enter(80, 1, self.process_manager.deactive_random_process())
        self.scheduler.enter(100, 1, self.process_manager.deactive_process(self.process_manager.get_coordenator()))
        self.scheduler.run()
        print(time.time())
