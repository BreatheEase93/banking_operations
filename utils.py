import json
from typing import List, Dict, Any
import os


def call_word_list(json_file :str)->List[Dict[str, Any]]:
    """Функция, которая принимает на вход путь до JSON-файла и возвращает список словарей с данными о финансовых транзакциях."""
    empty_list : list = []
    if not os.path.exists(json_file):
        return empty_list
    if not json_file.lower().endswith('.json'):
        return empty_list
    with open(json_file, 'r') as f:
        data = json.load(f)
        if not isinstance(data, list) or  data == empty_list:
            return empty_list
    return data