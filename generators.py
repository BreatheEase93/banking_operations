from typing import Any, Iterator


def filter_by_currency(list_of_dictionaries: list[dict[str, Any]], code: str) -> Iterator[dict[str, Any]]:
    """Гениратор возвращает итератор, который поочередно выдает транзакции,
    где валюта операции соответствует заданной (например, USD)."""
    if not list_of_dictionaries:
        return
    for transaction in list_of_dictionaries:
        try:
            if transaction["operationAmount"]["currency"]["code"] == code:
                yield transaction
        except (KeyError, TypeError):
            continue


def transaction_descriptions(list_of_dictionaries: list[dict[str, Any]]) -> Iterator[str]:
    """Генератор, который принимает список словарей с транзакциями и возвращает описание каждой операции по очереди."""
    if not list_of_dictionaries:
        return
    for transaction in list_of_dictionaries:
        try:
            description = transaction["description"]
            if description is not None:
                yield str(description)
        except (KeyError, TypeError):
            continue


def card_number_generator(start: int, finish: int) -> Iterator[str]:
    """Генератор, который выдает номера банковских карт в формате XXXX XXXX XXXX XXXX, где X
    — цифра номера карты. Генератор может сгенерировать номера карт в заданном диапазоне
    от 0000 0000 0000 0001 до 9999 9999 9999 9999."""
    if start is None or finish is None:
        return
    if not isinstance(start, int) or not isinstance(finish, int):
        return
    if not (0 < start <= finish <= 9999999999999999):
        return
    while start <= finish:
        card_str = f"{start:016d}"
        formatted = f"{card_str[:4]} {card_str[4:8]} {card_str[8:12]} {card_str[12:]}"
        yield formatted
        start += 1
