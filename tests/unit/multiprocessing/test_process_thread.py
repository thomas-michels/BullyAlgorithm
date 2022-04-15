"""
    Module for tests in ProcessThread
"""
import unittest
from unittest.mock import Mock, patch
from app.multiprocessing.process_thread import ProcessThread


class TestProcessThread(unittest.TestCase):
    """
    Test class for ProcessThread
    """

    @patch("app.multiprocessing.process_thread.sleep")
    def test_process_thread(self, sleep_mock):
        """
        Test in process thread
        """

        def function_test():
            quit()

        function_mock = Mock()
        function_mock.side_effect = function_test

        process_thread = ProcessThread(0, function_mock)
        process_thread.start()

        sleep_mock.assert_called_once_with(0)
        function_mock.assert_called_once()
