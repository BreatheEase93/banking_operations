from typing import Any

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
