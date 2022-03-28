"""
Application module
"""

from datetime import datetime, timedelta
from app.process_manager import ProcessManager
from app.election import BullyAlgorithm
import time


class Application:
    def __init__(self) -> None:
        self.process_manager = ProcessManager(BullyAlgorithm())
        self.run()

    def run(self) -> None:
        """
        Method to run Application

        :return:
            None
        """
        time_now = datetime.now()

        election = time_now + timedelta(seconds=25)
        new_process = time_now + timedelta(seconds=30)
        deactive_random_process = time_now + timedelta(seconds=80)
        deactive_coordenator = time_now + timedelta(seconds=100)

        while True:

            time_now = datetime.now()
            print(f"Hora atual - {time_now}")

            if election <= time_now:
                self.process_manager.send_request_to_coordenator()
                election = time_now + timedelta(seconds=25)

            if new_process <= time_now:
                self.process_manager.new_process()
                new_process = time_now + timedelta(seconds=30)

            if deactive_random_process <= time_now:
                self.process_manager.deactive_random_process()
                deactive_random_process = time_now + timedelta(seconds=80)

            if deactive_coordenator <= time_now:
                self.process_manager.deactive_process(
                    self.process_manager.get_coordenator()
                )
                deactive_coordenator = time_now + timedelta(seconds=100)

            print("#"*50)
            time.sleep(1)
