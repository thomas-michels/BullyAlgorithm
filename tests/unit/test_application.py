"""
    Module for tests in Application class
"""
import unittest

from unittest.mock import patch

from mock import call
from app.application import Application
from app.process_manager.process_manager import ProcessManager
from app.utils.time_now import show_time
from tests.mocks.thread_mock.process_thread_mock import ProcessThreadMock


class TestApplication(unittest.TestCase):
    """
    Class TestApplication
    """

    @patch("app.application.ProcessThread")
    def test_run(self, thread_mock):
        """
        Method to test 
        """
        thread_mock.side_effect = ProcessThreadMock

        app = Application()

        calls = [
            call(1, show_time),
            call(25, app.process_manager.send_request_to_coordenator),
            call(30, app.process_manager.new_process),
            call(80, app.process_manager.deactive_random_process),
            call(100, app.process_manager.deactive_coordenator),
        ]

        thread_mock.assert_has_calls(calls, any_order=False)
        self.assertEqual(thread_mock.call_count, 5)
