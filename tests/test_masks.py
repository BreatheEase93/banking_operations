from typing import Any

import pytest

from srs.masks import get_mask_account, get_mask_card_number


@pytest.mark.parametrize(
    "card_number, expected",
    [
        (121920193232323232401, "Неверные данные, только номер карты. Пример :1234567890123456"),
        ("121920wewrwerw23sdf12sf93401", "Неверные данные, только номер карты. Пример :1234567890123456"),
        ("121920193    401", "Неверные данные, только номер карты. Пример :1234567890123456"),
    ],
)
def test_get_mask_card_number(card_number: int, expected: str) -> Any:
    """Тест функции get_mask_card_number"""
    assert get_mask_card_number(card_number) == expected


def test_get_mask_card_number_all(card_number_1: int, empty_number: None, empty_list: list) -> Any:
    """Доп тест функции get_mask_card_number"""
    assert get_mask_card_number(card_number_1) == "7000 79** **** 6361"
    assert get_mask_card_number(empty_number) == "Неверные данные, только номер карты. Пример :1234567890123456"
    assert get_mask_card_number(empty_list) == "Неверные данные, только номер карты. Пример :1234567890123456"


@pytest.mark.parametrize(
    "account, expected",
    [
        (121920193232312121223232401, "Неверные данные, только номер счёта. Пример :12345678901234567890"),
        ("121920wewrwerw23sdf12sf93401", "Неверные данные, только номер счёта. Пример :12345678901234567890"),
        ("121920193    401", "Неверные данные, только номер счёта. Пример :12345678901234567890"),
    ],
)
def test_get_mask_account(account: int, expected: str) -> Any:
    """Тест функции get_mask_account"""
    assert get_mask_account(account) == expected


def test_get_mask_account_all(account_1: int, empty_number: None, empty_list: list) -> Any:
    """Доп тест функции get_mask_account`"""
    assert get_mask_account(account_1) == "**4305"
    assert get_mask_account(empty_number) == "Неверные данные, только номер счёта. Пример :12345678901234567890"
    assert get_mask_account(empty_list) == "Неверные данные, только номер счёта. Пример :12345678901234567890"
