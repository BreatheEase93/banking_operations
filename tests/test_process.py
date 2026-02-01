from srs.process import process_bank_operations, process_bank_search


def test_search_works(by_transactions_2):
    """Тест, что поиск работает."""
    assert len(process_bank_search(by_transactions_2, "Перевод")) == 1


def test_count_works(by_transactions_2):
    """Тест, что подсчет работает."""
    result = process_bank_operations(by_transactions_2, ["Перевод", "Организация"])
    assert result["Перевод"] == 1
    assert result["Организация"] == 1


def test_empty_search():
    """Тест пустого поиска."""
    assert process_bank_search([], "тест") == []
    assert process_bank_search([{"desc": "тест"}], "") == []


def test_empty_count():
    """Тест пустого подсчета."""
    assert process_bank_operations([], ["категория"]) == {"категория": 0}
