"""
    Module for tests in Request
"""
import unittest
from app.process.process import Process
from app.request.request import Request


class TestRequest(unittest.TestCase):
    """
    Tests in Request
    """

    def test_send_request_with_success(self):
        """
        Test request with success
        """

        sender = Process()
        receiver = Process()

        request = Request.send(sender, receiver)

        self.assertTrue(request)

    def test_send_request_sender_offline(self):
        """
        Test request failed because sender is offline
        """

        sender = Process()
        sender.change_status()
        receiver = Process()

        request = Request.send(sender, receiver)

        self.assertFalse(request)

    def test_send_request_receiver_not_exists(self):
        """
        Test request failed because receiver not exists
        """

        sender = Process()
        receiver = None

        request = Request.send(sender, receiver)

        self.assertFalse(request)
