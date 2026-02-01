import re


def process_bank_search(data:list[dict], search:str)->list[dict]:
    """Функция принимает список словарей с данными о банковских операциях и строку поиска,
     а возвращает список словарей, у которых в описании есть данная строка."""

    pattern = re.compile(search, flags=re.IGNORECASE)
    my_list: list[dict] = []
    for my_dict in data:
        for value in my_dict.values():
            if isinstance(value, str):
                if pattern.search(value):
                    my_list.append(my_dict)
                    break
    return my_list

