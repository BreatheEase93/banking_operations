from typing import Any


def filter_by_state(by_state: list[dict[str, Any]], state="EXECUTED") -> list[dict[str, Any]]:
    """Функция возвращает новый список словарей, содержащий только те словари, у которых ключ state"""
    new_by_state = list[dict[str, Any]]
    for dictionary in by_state:
        if dictionary.get("state") == state:
            new_by_state += dictionary
    return new_by_state
