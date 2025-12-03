from typing import Any


def filter_by_state(by_state: list[dict[str, Any]], state: str="EXECUTED") -> list[dict[str, Any]]:
    """Функция возвращает новый список словарей, содержащий только те словари, у которых ключ state"""
    new_by_state:   list[dict[str, Any]] =[]
    for item in by_state:
      if item.get("state") == state:
            new_by_state.append(item)
    return new_by_state


def sort_by_date(by_state: list[dict[str, Any]], decreasing: bool= True) -> list[dict[str, Any]]:
    """Функция возвращает новый список, отсортированный по дате (date)."""
    sorted_by_date: list[dict[str, Any]] = sorted(by_state, key=lambda x: x['date'], reverse=decreasing)
    return sorted_by_date

