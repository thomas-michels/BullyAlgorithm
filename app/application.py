"""
Application module
"""

class Application:

    def run(self):
        """ """

        print(f"Sistema Iniciado - {datetime.now()}")
        new_process = Timer(30, self.new_process())
        new_process.start()

        request_to_coordenator = Timer(
            25, self.election_time()
        )
        request_to_coordenator.start()

        inactive_coordenator = Timer(100, self.__coordenator.change_status())
        inactive_coordenator.start()

        inactive_process = Timer(80, choice(self.get_processes()).change_status())
        inactive_process.start()
