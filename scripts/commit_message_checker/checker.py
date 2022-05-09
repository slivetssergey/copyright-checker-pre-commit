#!/usr/bin/env python3

import argparse
import pathlib
import re
import sys
from typing import Optional, Sequence

from scripts.utils import Level, print_message


def parse_args(args: Optional[Sequence[str]] = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "COMMIT_EDITMSG",
        nargs="*",
        help="COMMIT_EDITMSG file path",
    )
    parser.add_argument(
        "--pattern",
        default="",
        required=False,
        help="Pattern for checking",
    )
    parser.add_argument(
        "--min_length",
        default=None,
        type=int,
        required=False,
        help="Minimum chars in commit message",
    )
    parser.add_argument(
        "--max_length",
        default=None,
        type=int,
        required=False,
        help="Maximum chars in commit message",
    )
    arguments = parser.parse_args(args)
    return arguments


def check(args: Optional[Sequence[str]] = None) -> int:
    arguments = parse_args(args)

    commit_editmsg = pathlib.Path(arguments.COMMIT_EDITMSG[0]).read_text()
    commit_message = " ".join(
        [i.strip() for i in commit_editmsg.split("\n") if i and not i.strip().startswith("#")]
    )

    err_msg = None
    if not commit_message:
        err_msg = "No commit message"

    message_length = len(commit_message)
    if arguments.min_length and message_length < arguments.min_length:
        err_msg = f"There should at least {arguments.min_length} chars in your commit message."

    if arguments.max_length and message_length > arguments.max_length:
        err_msg = f"There should maximum {arguments.max_length} chars in your commit message."

    if arguments.pattern and not re.search(rf"{arguments.pattern}", commit_message):
        err_msg = "Commit message does not match with template"

    if err_msg:
        print_message(err_msg, Level.ERROR)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(check())
