import srs.masks


def mask_account_card(account_card: str) -> str:
    """Функция принимающяя тип и номер карты или счета, возвращать строку с замаскированным номером"""
    account_card_split = account_card.split()
    for i, word in enumerate(account_card_split):
        if word.isdigit():
            if len(word) == 20:
                account_card_split[i] = srs.masks.get_mask_account(int(word))
            if len(word) == 16:
                account_card_split[i] = srs.masks.get_mask_card_number(int(word))
    account_card = " ".join(account_card_split)
    return account_card


def get_date(date: str) -> str:
    """Меняет формат даты"""
    new_date = f"{date[8:10]}.{date[5:7]}.{date[:4]}"
    return new_date
