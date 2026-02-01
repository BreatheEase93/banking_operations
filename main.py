from typing import Union,List, Dict, Any


from get_valid import get_valid
from srs.utils import call_word_list
from srs.process import process_bank_search
from srs.processing import filter_by_state, sort_by_date
from generators import filter_by_currency
from srs.utils_csv_xlsx import read_transactions_from_csv, read_transactions_from_excel
def main():
    print("""Программа: Привет! Добро пожаловать в программу работы
с банковскими транзакциями.
Выберите необходимый пункт меню:
1. Получить информацию о транзакциях из JSON-файла
2. Получить информацию о транзакциях из CSV-файла
3. Получить информацию о транзакциях из XLSX-файла""")
    num: Union[int, None] = get_valid(1,2,3)
    my_list:List[Dict] = []
    if num is None:
        return "Программа завершена досрочно. До свидание!"
    if num == 1:
        print("Для обработки выбран JSON-файл.")
        my_list = call_word_list("data/operations.json")

    if num == 2:
        print("Для обработки выбран CSV-файл.")
        my_list = read_transactions_from_csv("data/transactions.csv")
    if num == 3:
        print("Для обработки выбран XLSX-файл.")
        my_list = read_transactions_from_excel("data/transactions_excel.xlsx")
    print("""Введите статус, по которому необходимо выполнить фильтрацию. 
Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING""")
    status: Union[str, None] = get_valid("executed", "canceled", "pending")
    if status is None:
        return "Программ завершена досрочно. До свидание!"
    my_list = filter_by_state(my_list,status.upper())
    print(" Отсортировать операции по дате? Да/Нет")
    sort_1: Union[str, None] = get_valid("да", "нет")
    if sort_1 is None:
        return "Программ завершена досрочно. До свидание!"
    if sort_1 == "да":
        print("Отсортировать по возрастанию или по убыванию?")
        sort_2: Union[str, None] = get_valid("по возрастанию", "по убыванию")
        if sort_2 is None:
            return "Программ завершена досрочно. До свидание!"
        if sort_2 == "по возрастанию":
            my_list = sort_by_date(my_list)
        else:
            my_list = sort_by_date(my_list, False)
    print(" Выводить только рублевые транзакции? Да/Нет")
    sort_3: Union[str, None] = get_valid("да", "нет")
    if sort_3 is None:
        return "Программ завершена досрочно. До свидание!"
    if sort_3 == "да":
        my_list = list(filter_by_currency(my_list, "RUB"))






    return print(my_list)

main()
