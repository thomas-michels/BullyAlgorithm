"""
    Module for test in time now
"""
import unittest
from unittest.mock import patch
from app.utils.time_now import show_time


class TestShowTime(unittest.TestCase):
    """
    Tests for ShowTime function
    """

    @patch("app.utils.time_now.print")
    def test_show_time(self, print_mock):
        """
        Test in show time
        """

        self.assertIsNone(show_time())
        print_mock.assert_called_once()
