"""
Application module
"""

from datetime import datetime
from app.process_manager import ProcessManager
from app.election import BullyAlgorithm
from app.multiprocessing import ProcessThread


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
        time_now = ProcessThread(1, self.show_time)
        request_coordenator = ProcessThread(25, self.process_manager.send_request_to_coordenator)
        new_process = ProcessThread(30, self.process_manager.new_process)
        deactive_random = ProcessThread(80, self.process_manager.deactive_random_process)
        deactive_coordenator = ProcessThread(100, self.process_manager.deactive_coordenator)

        time_now.start()
        request_coordenator.start()
        new_process.start()
        deactive_random.start()
        deactive_coordenator.start()
        time_now.join()
        request_coordenator.join()
        new_process.join()
        deactive_random.join()
        deactive_coordenator.join()


    def show_time(self):
        print(f"Hora atual - {datetime.now()}")
