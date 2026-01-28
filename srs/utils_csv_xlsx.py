import pandas as pd
from typing import Any, Dict, List


def read_transactions_from_csv(file_csv: str) -> List[Dict[str, Any]]:
    """Функция, которая принимает на вход путь до csv-файла и
    возвращает список словарей с данными о финансовых транзакциях."""
    try:
        df = pd.read_csv(file_csv)
        transactions = df.to_dict(orient="records")
        return transactions
    except FileNotFoundError:
        raise FileNotFoundError(f"Файл '{file_csv}' не найден.")
    except Exception as e:
        raise Exception(f"Ошибка при обработке CSV-файла: {e}")


def read_transactions_from_excel(file_xlsx: str) -> List[Dict[str, Any]]:
    """Функция, которая принимает на вход путь до xlsx-файла и
    возвращает список словарей с данными о финансовых транзакциях."""
    try:
        df = pd.read_excel(file_xlsx)
        transactions = df.to_dict(orient="records")
        return transactions
    except FileNotFoundError:
        raise FileNotFoundError(f"Файл '{file_xlsx}' не найден.")
    except Exception as e:
        raise Exception(f"Ошибка при обработке Excel-файла: {e}")
