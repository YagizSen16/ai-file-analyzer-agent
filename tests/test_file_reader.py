import pytest
from src.file_reader import read_text_file


def test_read_text_file_success(tmp_path):
    test_file = tmp_path / "sample.txt"
    test_file.write_text("This is a test file.", encoding="utf-8")

    result = read_text_file(str(test_file))

    assert result == "This is a test file."


def test_read_text_file_not_found():
    with pytest.raises(FileNotFoundError):
        read_text_file("missing_file.txt")


def test_read_text_file_empty(tmp_path):
    test_file = tmp_path / "empty.txt"
    test_file.write_text("", encoding="utf-8")

    with pytest.raises(ValueError):
        read_text_file(str(test_file))


def test_read_text_file_wrong_extension(tmp_path):
    test_file = tmp_path / "sample.pdf"
    test_file.write_text("This should not be accepted.", encoding="utf-8")

    with pytest.raises(ValueError):
        read_text_file(str(test_file))