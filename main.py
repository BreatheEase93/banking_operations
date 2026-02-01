from typing import Any, Dict, Hashable, List, Optional, Union

from generators import filter_by_currency
from get_valid import get_valid
from srs.process import process_bank_search
from srs.processing import filter_by_state, sort_by_date
from srs.utils import call_word_list
from srs.utils_csv_xlsx import read_transactions_from_csv, read_transactions_from_excel
from srs.widget import get_date, mask_account_card


def main() -> None:
    print(
        """Программа: Привет! Добро пожаловать в программу работы
с банковскими транзакциями.
Выберите необходимый пункт меню:
1. Получить информацию о транзакциях из JSON-файла
2. Получить информацию о транзакциях из CSV-файла
3. Получить информацию о транзакциях из XLSX-файла"""
    )
    num: Optional[Union[int, str]] = get_valid(1, 2, 3)
    my_list: List[Dict[str, Any]] | list[dict[Hashable, Any]] = []
    if num is None:
        print("Программа завершена досрочно. До свидания!")
        return
    if num == 1:
        print("Для обработки выбран JSON-файл.")
        my_list = call_word_list("data/operations.json")

    elif num == 2:
        print("Для обработки выбран CSV-файл.")
        my_list = read_transactions_from_csv("data/transactions.csv")
    else:
        print("Для обработки выбран XLSX-файл.")
        my_list = read_transactions_from_excel("data/transactions_excel.xlsx")
    print(
        """Введите статус, по которому необходимо выполнить фильтрацию.
Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING"""
    )
    status: Optional[Union[int, str]] = get_valid("executed", "canceled", "pending")
    if status is None:
        print("Программа завершена досрочно. До свидания!")
        return
    filter_my_list: List[Dict[str, Any]] = filter_by_state(my_list, str(status).upper())
    print("Отсортировать операции по дате? Да/Нет")
    sort_1: Optional[Union[int, str]] = get_valid("да", "нет")
    if sort_1 is None:
        print("Программа завершена досрочно. До свидания!")
        return
    if sort_1 == "да":
        print("Отсортировать по возрастанию или по убыванию?")
        sort_2: Optional[Union[int, str]] = get_valid("по возрастанию", "по убыванию")
        if sort_2 is None:
            print("Программа завершена досрочно. До свидания!")
            return
        if sort_2 == "по возрастанию":
            sort_my_list: List[Dict[str, Any]] = sort_by_date(filter_my_list, False)
        else:
            sort_my_list: List[Dict[str, Any]] = sort_by_date(
                filter_my_list,
            )
    else:
        sort_my_list: List[Dict[str, Any]] = filter_my_list
    print("Выводить только рублевые транзакции? Да/Нет")
    sort_3: Optional[Union[int, str]] = get_valid("да", "нет")
    if sort_3 is None:
        print("Программа завершена досрочно. До свидания!")
        return
    if sort_3 == "да":
        sort_1_my_list: List[Dict[str, Any]] = list(filter_by_currency(sort_my_list, "RUB"))
    else:
        sort_1_my_list: List[Dict[str, Any]] = sort_my_list
    print("Отфильтровать список транзакций по определенному слову в описании? Да/Нет")
    sort_4: Optional[Union[int, str]] = get_valid("да", "нет")
    if sort_4 is None:
        print("Программа завершена досрочно. До свидания!")
        return
    if sort_4 == "да":
        search: str = input("Введите слово для поиска в описании или 'стоп'")
        if search.lower() == "стоп":
            print("Программа завершена досрочно. До свидания!")
            return
        sort_2_my_list: List[Dict[str, Any]] = list(process_bank_search(sort_1_my_list, search))
    else:
        sort_2_my_list: List[Dict[str, Any]] = sort_1_my_list
    print(f"Всего банковских операций в выборке: {len(sort_2_my_list)}")
    if not sort_2_my_list:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
        return
    if num == 1:
        for transaction in sort_2_my_list:
            date: str = get_date(transaction["date"])
            description: str = transaction["description"]
            from_transaction: str = mask_account_card(transaction.get("from", ""))
            to_transaction: str = mask_account_card(transaction.get("to", ""))
            amount: str = transaction["operationAmount"]["amount"]
            name: str = transaction["operationAmount"]["currency"]["name"]
            if (
                from_transaction != "Неверные данные, счет и номер или тип карты и номер."
                " Пример "
                ":Maestro 1234567890123456 Счет 12345678901234567890"
            ):
                print(
                    f"""{date} {description}
{from_transaction} -> {to_transaction}
Сумма: {amount} {name}
    """
                )
            else:
                print(
                    f"""{date} {description}
{to_transaction}
Сумма: {amount} {name}
"""
                )
    else:
        for transaction in sort_2_my_list:
            date: str = get_date(transaction["date"])
            description: str = transaction["description"]
            from_transaction: str = mask_account_card(transaction.get("from", ""))
            to_transaction: str = mask_account_card(transaction.get("to", ""))
            amount: str = transaction["amount"]
            name: str = transaction["currency_name"]
            if (
                from_transaction != "Неверные данные, счет и номер или тип карты и номер. "
                "Пример :Maestro 1234567890123456 Счет 12345678901234567890"
            ):
                print(
                    f"""{date} {description}
{from_transaction} -> {to_transaction}
Сумма: {amount} {name}
"""
                )
            else:
                print(
                    f"""{date} {description}
{to_transaction}
Сумма: {amount} {name}
"""
                )

    return
