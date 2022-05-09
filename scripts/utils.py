from enum import Enum


class Level(str, Enum):
    OK = "OK"
    INFO = "INFO"
    WARNING = "WARNING"
    ERROR = "ERROR"


class Color(str, Enum):
    OK = "\033[92m"
    INFO = "\033[94m"
    WARNING = "\033[93m"
    ERROR = "\033[91m"


def print_message(message: str, level: Level = Level.OK) -> None:
    msg = f"{Color[level]}{level}: {message}"
    print(msg)
