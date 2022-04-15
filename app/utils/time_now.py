"""
    Module for show time function
"""

from datetime import datetime


def show_time() -> None:
    """
    Function to show current time

    :return: None
    """
    print(f"Hora atual - {datetime.now()}")
