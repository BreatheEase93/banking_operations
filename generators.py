from typing import Any, Iterator


def filter_by_currency(list_of_dictionaries: list[dict[str, Any]], code: str) -> Iterator[dict[str, Any]]:
    """Функция возвращает итератор, который поочередно выдает транзакции,
    где валюта операции соответствует заданной (например, USD)."""

    for transaction in list_of_dictionaries:
        if transaction['operationAmount']['currency']['code'] == code:
            yield transaction

def transaction_descriptions(list_of_dictionaries: list[dict[str, Any]]) -> Iterator[str]:
    """Генератор который принимает список словарей с транзакциями и возвращает описание каждой операции по очереди."""
    for transaction in list_of_dictionaries:
        yield transaction["description"]


def card_number_generator(start: int, finish: int)-> Iterator[str]:
    """Генератор который выдает номера банковских карт в формате XXXX XXXX XXXX XXXX, где X
    — цифра номера карты. Генератор может сгенерировать номера карт в заданном диапазоне
    от 0000 0000 0000 0001 до 9999 9999 9999 9999."""
    if start <= finish and finish < 10000000000000000 and start > 0 and finish >= 0:
      while start <= finish:
          list_start = list("{:016d}".format(start))
          list_start.insert(4, " ")
          list_start.insert(9, " ")
          list_start.insert(14, " ")
          list_start_new = "".join(list_start)
          yield list_start_new
          start += 1
