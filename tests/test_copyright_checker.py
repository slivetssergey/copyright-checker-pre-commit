import pathlib

import pytest

from scripts.copyright_checker.checker import CopyrightChecker
from scripts.copyright_checker.exceptions import CopyrightFileNotFoundException


class TestCopyrightChecker:
    def test_not_exists_copyright_file(self, test_file):
        with pytest.raises(CopyrightFileNotFoundException):
            CopyrightChecker(
                copyright_file=pathlib.Path("not_exists_file.txt"), filenames=[test_file()]
            )

    def test_valid_file(self, test_file, copyright_file, copyright_content):
        assert CopyrightChecker(
            copyright_file=copyright_file(), filenames=[test_file(copyright_content)]
        ).check()

    def test_invalid_file(self, test_file, copyright_file):
        assert not CopyrightChecker(
            copyright_file=copyright_file(), filenames=[test_file()]
        ).check()

    def test_regex_copyright(self, test_file, copyright_file):
        regex_copyright = "# Copyright 202[0-9]"
        file_copyright = "# Copyright 2022"
        assert CopyrightChecker(
            copyright_file=copyright_file(regex_copyright), filenames=[test_file(file_copyright)]
        ).check()

    def test_shebang(self, test_file, copyright_file, copyright_content):
        shebang = "#!/usr/bin/env python3\n"
        file_copyright = shebang + copyright_content
        assert CopyrightChecker(
            copyright_file=copyright_file(), filenames=[test_file(file_copyright)]
        ).check()

    def test_with_empty_first_string(self, test_file, copyright_file, copyright_content):
        file_copyright = "\n" + copyright_content
        assert not CopyrightChecker(
            copyright_file=copyright_file(), filenames=[test_file(file_copyright)]
        ).check()
