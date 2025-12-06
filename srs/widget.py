import srs.masks
from datetime import datetime


def mask_account_card(account_card: str) -> str:
    """Функция принимающяя тип и номер карты или счета, возвращать строку с замаскированным номером"""
    if isinstance(account_card, str):
        account_card_split = account_card.split()
        for i, word in enumerate(account_card_split):
            if word.isdigit():
                if len(word) == 20:
                    account_card_split[i] = srs.masks.get_mask_account(int(word))
                if len(word) == 16:
                    account_card_split[i] = srs.masks.get_mask_card_number(int(word))
        account_card = " ".join(account_card_split)
        return account_card
    return "Неверные данные, счет и номер или тип карты и номер. Пример :Maestro 1234567890123456 Счет 12345678901234567890"


def get_date(date_string: str) -> str:
    """Меняет формат даты"""
    try:
        date_object = datetime.strptime(date_string, '%Y-%m-%dT%H:%M:%S.%f')
        date_object_new = datetime.strftime(date_object, "%d.%m.%Y")
        return str(date_object_new)
    except TypeError:
        return "Неверные данные. Пример: 2024-03-11T02:26:18.671407"
    except ValueError:
        return "Неверные данные. Пример: 2024-03-11T02:26:18.671407"
