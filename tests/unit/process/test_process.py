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
        """
        p1, p2 = self.__instance_process()

        self.assertFalse(p1.is_active())
        self.assertFalse(p2.is_active())

        p1.change_status()

        self.assertTrue(p1.is_active())

    def test_ids(self):
        """
        """
        p1, p2 = self.__instance_process()

        self.assertEqual(p1.get_id(), 1)
        self.assertEqual(p2.get_id(), 2)
