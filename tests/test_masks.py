import pytest
from srs.masks import get_mask_card_number, get_mask_account
from tests.conftest import card_number_1, empty_number


@pytest.mark.parametrize("card_number, expected", [
    (121920193232323232401, "Неверные данные, только номер карты. Пример :1234567890123456"),
    ("121920wewrwerw23sdf12sf93401", "Неверные данные, только номер карты. Пример :1234567890123456"),
    ("121920193    401", "Неверные данные, только номер карты. Пример :1234567890123456"),
])


def test_get_mask_card_number(card_number,empty_number, card_number_1, expected):
    assert get_mask_card_number(card_number_1) == "7000 79** **** 6361"
    assert get_mask_card_number(empty_number) == "Неверные данные, только номер карты. Пример :1234567890123456"
    assert get_mask_card_number(card_number) == expected

