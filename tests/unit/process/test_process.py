"""
Module to test Process class
"""
from typing import Tuple
import unittest
from app.process import Process


class TestProcess(unittest.TestCase):
    """
    Test Process class
    """

    def __instance_process(self) -> Tuple[Process, Process]:
        return Process(), Process()

    def test_change_status(self):
        """
        Test to check status is changed
        """
        p1, p2 = self.__instance_process()

        self.assertTrue(p1.is_active())
        self.assertTrue(p2.is_active())

        p1.change_status()

        self.assertFalse(p1.is_active())

    def test_ids(self):
        """
        Test to check if ids are diferent
        """
        p1, p2 = self.__instance_process()

        self.assertGreater(p2.get_id(), p1.get_id())

    def test_send_request(self):
        """
        Test send request
        """
        p1, p2 = self.__instance_process()

        self.assertTrue(p1.send_request(p2))

        p1.change_status()

        self.assertFalse(p2.send_request(p1))
        self.assertFalse(p1.send_request(p2))
