import os
from typing import Any

import requests
from dotenv import load_dotenv

load_dotenv(".env")


def withdrawal_of_the_amount(transaction: dict[str, Any]) -> float:
    amount = float(transaction["operationAmount"]["amount"])
    code = transaction["operationAmount"]["currency"]["code"]
    if code == "RUB":
        return amount
    else:
        try:
            url = f"https://api.apilayer.com/exchangerates_data/latest?base={code}&symbols=RUB"

            headers = {"apikey": os.getenv("API_KEY")}
            response = requests.get(url, headers=headers, timeout=10)
            response.raise_for_status()
            result = response.json()
            exchange_rate = float(result["rates"]["RUB"])
            return amount * exchange_rate
        except requests.exceptions.ConnectionError:
            print("Ошибка подключения к серверу")
            return 0
        except requests.exceptions.Timeout:
            print("Превышено время ожидания ответа")
            return 0
        except requests.exceptions.HTTPError as e:
            print(f"HTTP ошибка: {e}")
            return 0
        except Exception as e:
            print(f"Неизвестная ошибка: {e}")
            return 0
