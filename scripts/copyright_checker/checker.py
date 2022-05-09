#!/usr/bin/env python3

import argparse
import pathlib
import re
import sys
from typing import List, Optional, Sequence

from scripts.copyright_checker.exceptions import (
    CopyrightCheckerException,
    CopyrightFileNotFoundException,
)
from scripts.utils import Level, print_message


class CopyrightChecker:
    def __init__(self, filenames: List[pathlib.Path], copyright_file: pathlib.Path):
        self.copyright = self.read_copyright_file(copyright_file)
        self.filenames = filenames

    def read_copyright_file(self, copyright_file: pathlib.Path) -> str:
        try:
            return copyright_file.read_text().strip()
        except FileNotFoundError:
            raise CopyrightFileNotFoundException(f"Copyright file {copyright_file} not found")

    def check_file_copyright(self, file: pathlib.Path) -> bool:
        file_data = pathlib.Path(file).read_text()
        try:
            shebang, body = file_data.split("\n", 1)
        except ValueError:
            shebang, body = file_data, ""

        if not shebang.startswith("#!"):
            body = file_data

        exist_copyright = re.search(self.copyright, body)
        return bool(exist_copyright and exist_copyright.start() == 0)

    def check(self) -> bool:
        is_valid = True
        for filename in self.filenames:
            if not self.check_file_copyright(filename):
                mgs = f"File {filename} does not contain a valid copyright notice."
                print_message(mgs, Level.ERROR)
                is_valid = False
        return is_valid


def parse_args(args: Optional[Sequence[str]] = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "filenames",
        nargs="*",
        help="Filenames for check",
    )
    parser.add_argument(
        "--copyright",
        default="copyright.txt",
        help="Path to file with copyright text",
    )
    arguments = parser.parse_args(args)
    return arguments


def check(args: Optional[Sequence[str]] = None) -> int:
    arguments = parse_args(args)
    filenames = [pathlib.Path(file) for file in arguments.filenames]
    copyright_file = pathlib.Path(arguments.copyright)
    try:
        result = CopyrightChecker(
            copyright_file=copyright_file,
            filenames=filenames,
        ).check()
        return 0 if result else 1
    except CopyrightCheckerException as exc:
        print_message(str(exc), Level.ERROR)
    return 1


if __name__ == "__main__":
    sys.exit(check())
