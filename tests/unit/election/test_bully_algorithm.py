"""
Module to test bully algorithm
"""

import unittest
from app.process import Process
from app.election import BullyAlgorithm


class TestBullyAlgorithm(unittest.TestCase):
    """
    Test BullyAlgorithm class
    """

    def test_election(self):
        """
        Test election is correct
        """

        bully = BullyAlgorithm()
        process_start = Process()
        processes = [Process(), process_start, Process()]
        higher_id = Process()
        processes.append(higher_id)

        coordenator = bully.run_election(process_start, processes)

        self.assertEqual(higher_id.get_id(), coordenator.get_id())
