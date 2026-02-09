from typing import Any
from unittest.mock import Mock, patch

import pytest


@pytest.fixture()
def card_number_1() -> int:
    """Пример номера карты"""
    return 7000792289606361


@pytest.fixture()
def account_1() -> int:
    """Пример номера счёта"""
    return 73654108430135874305


@pytest.fixture()
def empty_string() -> str:
    """Пустая строка"""
    return ""


@pytest.fixture()
def empty_list() -> list:
    """Пустой список"""
    return []


@pytest.fixture()
def empty_number() -> None:
    """Полное отсутствие значения"""
    return None


@pytest.fixture()
def by_state() -> list[dict[str, Any]]:
    """Список некоторой информации"""
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]


@pytest.fixture()
def by_transactions() -> list[dict[str, Any]]:
    """Список некоторых транзакций"""
    return [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188",
        },
        {
            "id": 873106923,
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404",
            "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 44812258784861134719",
            "to": "Счет 74489636417521191160",
        },
        {
            "id": 895315941,
            "state": "EXECUTED",
            "date": "2018-08-19T04:27:37.904916",
            "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод с карты на карту",
            "from": "Visa Classic 6831982476737658",
            "to": "Visa Platinum 8990922113665229",
        },
        {
            "id": 594226727,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
            "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод организации",
            "from": "Visa Platinum 1246377376343588",
            "to": "Счет 14211924144426031657",
        },
    ]


@pytest.fixture()
def by_transactions_1() -> list[dict[str, Any]]:
    """Транзакция"""
    return [
        {
            "id": 873106923,
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404",
            "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 44812258784861134719",
            "to": "Счет 74489636417521191160",
        }
    ]


@pytest.fixture()
def by_transactions_2() -> list[dict[str, Any]]:
    """Транзакция"""
    return [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        }
    ]


@pytest.fixture()
def invalid_transactions() -> list[dict]:
    """Транзакции с некорректной структурой"""
    return [
        {"id": 1, "operationAmount": {"amount": "100"}},  # нет currency
        {"id": 2, "operationAmount": {"currency": {"name": "USD"}}},  # нет code
    ]


@pytest.fixture()
def json_file() -> str:
    """Путь файла operations.json"""
    return "data/operations.json"


@pytest.fixture()
def mock_api_response():
    """Фикстура для мока ответа от API"""
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.raise_for_status = Mock()
    return mock_response


@pytest.fixture()
def csv_file() -> str:
    """Путь файла transactions.csv"""
    return "data/transactions.csvv"


@pytest.fixture()
def xlsx_file() -> str:
    """Путь файла transactions_excel.xlsx"""
    return "data/transactions_excel.xlsx"


@pytest.fixture()
def mock_csv_response():
    """Фикстура для мока ответа от csv файла"""
    mock_df = Mock()
    return mock_df


@pytest.fixture()
def mock_xlsx_response():
    """Фикстура для мока ответа от xlsx файла"""
    mock_df = Mock()
    return mock_df


@pytest.fixture
def valid_string_inputs():
    """Возвращает строки как допустимые аргументы"""
    return ["да", "нет", "возможно"]


@pytest.fixture
def valid_mixed_inputs():
    """Возвращает смешанные типы как допустимые аргументы"""
    return [1, 2, 3, "да", "нет"]


@pytest.fixture
def mock_input():
    """Фикстура для мока ввода"""
    return patch("builtins.input")
