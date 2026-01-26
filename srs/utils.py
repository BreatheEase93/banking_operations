import json
import logging
import os
from typing import Any, Dict, List

logger = logging.getLogger(__name__)
file_handler = logging.FileHandler(f"../logs/{__name__}.log", mode="w")
file_formatter = logging.Formatter("%(asctime)s %(module)s %(funcName)s %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


def call_word_list(json_file: str) -> List[Dict[str, Any]]:
    """Функция, которая принимает на вход путь до JSON-файла и
    возвращает список словарей с данными о финансовых транзакциях."""
    empty_list: list = []
    if not os.path.exists(json_file):
        logger.error("Неправильный путь к файлу")
        return empty_list
    if not json_file.lower().endswith(".json"):
        logger.error("Формат файла не .json")
        return empty_list
    with open(json_file, "r", encoding="utf-8") as f:
        data = json.load(f)
        if not isinstance(data, list):
            logger.error("В файле нет списка транзакций")
            return empty_list
    logger.info("Функция выполнена успешно")
    return data
