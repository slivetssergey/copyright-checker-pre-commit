#!/usr/bin/env python3

import argparse
import pathlib
import re
import sys
from typing import List, Optional, Sequence

from copyright_checker.exceptions import CopyrightCheckerException, CopyrightFileNotFoundException


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
                print(f"File {filename} does not contain a valid copyright notice.")
                is_valid = False
        return is_valid


def check(args: Optional[Sequence[str]] = None) -> int:
    # def check(args: Union[argparse.Namespace, Optional[Sequence[str]]] = None) -> int:
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
    filenames = [pathlib.Path(file) for file in arguments.filenames]
    copyright_file = pathlib.Path(arguments.copyright)
    try:
        result = CopyrightChecker(
            copyright_file=copyright_file,
            filenames=filenames,
        ).check()
        return 0 if result else 1
    except CopyrightCheckerException as exc:
        print(exc)
    return 1


if __name__ == "__main__":
    sys.exit(check())
