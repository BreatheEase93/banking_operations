import json
import os
import tempfile

from srs.utils import call_word_list


def tests_call_word_list(json_file):
    """Тесты с файлом operations.json функции call_word_list, а также длч некорректного адреса"""
    result = call_word_list(json_file)
    assert len(result) == 101
    assert result[0] == {
        "id": 441945886,
        "state": "EXECUTED",
        "date": "2019-08-26T10:50:58.294041",
        "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод организации",
        "from": "Maestro 1596837868705199",
        "to": "Счет 64686473678894779589",
    }
    assert call_word_list("sdasdadasd") == []


def test_call_word_list_not_json_extension():
    """Тест на файл с неправильным расширением"""
    with tempfile.NamedTemporaryFile(mode="w", suffix=".txt", delete=False) as f:
        json.dump([{"id": 1}], f)
        file_path = f.name

    try:
        result = call_word_list(file_path)
        assert result == []
    finally:
        os.unlink(file_path)


def test_call_word_list_empty_json():
    """Тест на пустой JSON файл"""
    with tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False) as f:
        json.dump([], f)
        file_path = f.name

    try:
        result = call_word_list(file_path)
        assert result == []
    finally:
        os.unlink(file_path)
