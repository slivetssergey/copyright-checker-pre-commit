import pathlib

import pytest


@pytest.fixture
def code_example():
    yield 'print("Hello world")'


@pytest.fixture
def test_file(tmp_path, code_example):
    def _create(copyright: str = None, filename: str = "check_me.py"):
        p = tmp_path / filename
        text = ""
        if copyright:
            text += copyright
        text += code_example
        p.write_text(text)
        return pathlib.Path(p)

    yield _create


@pytest.fixture
def copyright_content():
    yield """# Test copyright
    # Default copyright
    """


@pytest.fixture
def copyright_file(tmp_path, copyright_content):
    def _create(text: str = None):
        p = tmp_path / "copyright.txt"
        p.write_text(text or copyright_content)
        return pathlib.Path(p)

    yield _create
