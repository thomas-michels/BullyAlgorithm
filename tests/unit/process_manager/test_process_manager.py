"""
    Module for tests in ProcessManager
"""
import unittest
from unittest.mock import Mock, patch
from mock import call
from app.process_manager.process_manager import ProcessManager
from tests.mocks.election_mock.election_mock import ElectionMock


class TestProcessManager(unittest.TestCase):
    """
    Tests for ProcessManager class
    """

    def setUp(self) -> None:
        self.pm = ProcessManager(election_algotithm=ElectionMock())

    @patch("app.process_manager.process_manager.print")
    def test_get_processes(self, print_mock):
        """
        Test in method get processes
        """

        process = self.pm.new_process()

        processes = self.pm.get_processes()
        self.assertEqual(len(processes), 1)
        print_mock.assert_called_once_with(f"O Processo com o ID {process.get_id()} foi criado!")

    @patch("app.process_manager.process_manager.print")
    def test_get_active_processs(self, print_mock):
        """
        Test in method get active processes
        """

        process = self.pm.new_process()
        process2 = self.pm.new_process()
        process2.change_status()

        calls = [
            call(f"O Processo com o ID {process.get_id()} foi criado!"),
            call(f"O Processo com o ID {process2.get_id()} foi criado!"),
        ]

        processes = self.pm.get_active_processes()
        self.assertEqual(len(processes), 1)
        print_mock.assert_has_calls(calls)

    @patch("app.process_manager.process_manager.print")
    def test_deactive_random_process(self, print_mock):
        """
        Test in method deactive random process
        """

        process = self.pm.new_process()

        calls = [
            call(f"O Processo com o ID {process.get_id()} foi criado!"),
            call(f"O processo com o ID {process.get_id()} foi desativado!"),
        ]

        self.assertIsNone(self.pm.deactive_random_process())
        self.assertFalse(process.is_active())
        print_mock.assert_has_calls(calls)

    @patch("app.process_manager.process_manager.print")
    def test_deactive_coordenator(self, print_mock):
        """
        Test in method deactive coordenator
        """

        process = self.pm.new_process()
        self.pm.set_coordenator(process)

        calls = [
            call(f"O Processo com o ID {process.get_id()} foi criado!"),
            call(f"O coordenador com o ID {process.get_id()} foi desativado!"),
        ]

        self.assertIsNone(self.pm.deactive_coordenator())
        self.assertFalse(self.pm.get_coordenator().is_active())
        print_mock.assert_has_calls(calls)

    @patch("app.process_manager.process_manager.print")
    def test_deactive_coordenator_with_coordenator_was_deactivated(self, print_mock):
        """
        Test in method deactive coordenator with coordenator was deactivated
        """

        process = self.pm.new_process()
        process.change_status()
        self.pm.set_coordenator(process)

        calls = [
            call(f"O Processo com o ID {process.get_id()} foi criado!"),
            call(f"O coordenador já está inativo"),
        ]

        self.assertIsNone(self.pm.deactive_coordenator())
        self.assertFalse(self.pm.get_coordenator().is_active())
        print_mock.assert_has_calls(calls)

    def test_send_request_to_coordenator_without_active_process(self):
        """
        Test in method send request to coordenator without active process
        """

        self.assertIsNone(self.pm.send_request_to_coordenator())

    @patch("app.process_manager.process_manager.print")
    def test_send_request_to_coordenator(self, print_mock):
        """
        Test in send request to coordenator
        """

        process = self.pm.new_process()

        calls = [
            call(f"O Processo com o ID {process.get_id()} foi criado!"),
            call(f"Mensagem enviada do processo {process.get_id()} para o Coordenador - Negada")
        ]

        self.assertIsNone(self.pm.get_coordenator())
        self.assertIsNone(self.pm.send_request_to_coordenator())
        self.assertEqual(process, self.pm.get_coordenator())
        print_mock.assert_has_calls(calls)
