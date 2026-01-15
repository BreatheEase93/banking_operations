from generators import filter_by_currency, transaction_descriptions, card_number_generator


def test_filter_by_currency_all(by_transactions, empty_list, invalid_transactions):
    """Тесты функции filter_by_currency"""
    # проверка работоспособности
    assert next(filter_by_currency(by_transactions, "USD")) == {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {
            "amount": "9824.07",
            "currency": {
                "name": "USD",
                "code": "USD"
            }
        },
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702"
    }
    assert len(list(filter_by_currency(by_transactions, "USD"))) == 3
    assert len(list(filter_by_currency(by_transactions, "RUB"))) == 2

    # Пустые итераторы
    assert list(filter_by_currency(empty_list, "USD")) == []
    assert list(filter_by_currency(invalid_transactions, "USD")) == []
    assert list(filter_by_currency(by_transactions, "EUR")) == []
    assert list(filter_by_currency(by_transactions, "")) == []


def test_transaction_descriptions_all(by_transactions, empty_list):
    """Тесты функции transaction_descriptions"""
    # проверка работоспособности
    assert next(transaction_descriptions(by_transactions)) == "Перевод организации"
    result = list(transaction_descriptions(by_transactions))
    assert len(result) == 5

    # Пустые итераторы
    assert list(transaction_descriptions(empty_list)) == []
    no_desc = [{"id": 1}, {"operationAmount": {"amount": "100"}}]
    assert list(transaction_descriptions(no_desc)) == []


def test_card_number_generator_compact():
    """Краткие тесты генератора карт"""
    # проверка работоспособности
    assert next(card_number_generator(1, 1)) == "0000 0000 0000 0001"
    assert len(list(card_number_generator(1, 10))) == 10
    assert next(card_number_generator(9999999999999999, 9999999999999999)) == "9999 9999 9999 9999"

    # Пустые итераторы
    assert list(card_number_generator(0, 1)) == []
    assert list(card_number_generator(2, 1)) == []
    assert list(card_number_generator(None, 1)) == []