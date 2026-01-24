import os
import requests
from dotenv import load_dotenv
from typing import Any

load_dotenv('.env')

def withdrawal_of_the_amount(transaction: dict[str, Any])->float:
    amount = float(transaction["operationAmount"]["amount"])
    code = transaction["operationAmount"]["currency"]["code"]
    if code == 'RUB':
        return amount
    else:
        try:
            url = f"https://api.apilayer.com/exchangerates_data/latest?base={code}&symbols=RUB"

            headers = {"apikey": os.getenv('API_KEY')}
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

test = withdrawal_of_the_amount({
    "id": 41428829,
    "state": "EXECUTED",
    "date": "2019-07-03T18:35:29.512364",
    "operationAmount": {
      "amount": "8221.37",
      "currency": {
        "name": "USD",
        "code": "USD"
      }
    },
    "description": "Перевод организации",
    "from": "MasterCard 7158300734726758",
    "to": "Счет 35383033474447895560"
})
print(test)











# load_dotenv('.env')
#
#
# url = "https://api.apilayer.com/exchangerates_data/latest?symbols=Usd%2C%20EUR&base=Rub"
#
# payload = {}
# headers= {
#   "apikey": os.getenv('API_KEY')
# }
#
# response = requests.request("GET", url, headers=headers, data = payload)
#
# status_code = response.status_code
# result = response.text
# print(result)