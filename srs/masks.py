def get_mask_card_number(card_number: int) -> str:
    """Функция принимает на вход номер карты и возвращает её маску"""
    if  isinstance(card_number, int):
        card_number_string = str(card_number)
        if len(card_number_string) == 16:
            card_number_list = list(card_number_string)
            card_number_list[6:12] = ["*", "*", "*", "*", "*", "*"]
            card_number_list.insert(4, " ")
            card_number_list.insert(9, " ")
            card_number_list.insert(14, " ")
            card_number_string_new = "".join(card_number_list)
            return card_number_string_new
    return "Неверные данные, только номер карты. Пример :1234567890123456"


def get_mask_account(account: int) -> str:
    """Функция принимает на вход номер счёта и возвращает его маску"""
    if isinstance(account, int):
        account_string = str(account)
        if len(account_string) == 20:
            account_list = list(account_string)
            account_list[:-4] = ["*", "*"]
            account_list_new = "".join(account_list)
            return account_list_new
    return "Неверные данные, только номер счёта. Пример :12345678901234567890"
