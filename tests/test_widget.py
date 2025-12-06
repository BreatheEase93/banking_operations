import pytest
from srs.widget import mask_account_card


@pytest.mark.parametrize("account_card, expected", [
    ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
    ("Счет 64686473678894779589","Счет **9589"),
    ("MasterCard 7158300734726758", "MasterCard 7158 30** **** 6758"),
    ("Счет 35383033474447895560", "Счет **5560"),
    ("Visa Classic 6831982476737658", "Visa Classic 6831 98** **** 7658"),
    ("Visa Platinum 8990922113665229", "Visa Platinum 8990 92** **** 5229"),
    ("Visa Gold 5999414228426353", "Visa Gold 5999 41** **** 6353"),
    ("Счет 73654108430135874305", "Счет **4305"),
])

def test_mask_account_card(account_card, expected):
    assert mask_account_card(account_card) == expected


def test_mask_account_card_all(empty_list, empty_number):
    assert mask_account_card(empty_list) == "Неверные данные, счет и номер или тип карты и номер. Пример :Maestro 1234567890123456 Счет 12345678901234567890"
    assert mask_account_card(empty_number) == "Неверные данные, счет и номер или тип карты и номер. Пример :Maestro 1234567890123456 Счет 12345678901234567890"