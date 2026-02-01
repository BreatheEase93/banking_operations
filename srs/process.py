import re
from collections import Counter

from generators import transaction_descriptions


def process_bank_search(data: list[dict], search: str) -> list[dict]:
    """Функция принимает список словарей с данными о банковских операциях и строку поиска,
    а возвращает список словарей, у которых в описании есть данная строка."""

    if not data or not search:
        return []

    pattern = re.compile(re.escape(search), re.IGNORECASE)
    result = []

    for i, description in enumerate(transaction_descriptions(data)):
        if pattern.search(description):
            result.append(data[i])

    return result


def process_bank_operations(data: list[dict], categories: list) -> dict:
    """Функция, которая принимает список словарей с данными о банковских операциях и список категорий операций,
    а возвращает словарь, в котором ключи — это названия категорий,
    а значения — это количество операций в каждой категории.
    """

    counted: Counter[str] = Counter()

    patterns = {category: re.compile(category, flags=re.IGNORECASE) for category in categories}

    for description in transaction_descriptions(data):
        for category, pattern in patterns.items():
            if pattern.search(description):
                counted[category] += 1

    return {category: counted.get(category, 0) for category in categories}
