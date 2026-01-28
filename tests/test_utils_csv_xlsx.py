import pytest
from unittest.mock import patch
from srs.utils_csv_xlsx import read_transactions_from_csv, read_transactions_from_excel


def run_test_read_transactions_from_csv(csv_file: str, mock_csv_response):
    """Тест успешного чтения CSV файла"""
    mock_df = mock_csv_response
    mock_df.to_dict.return_value = [
        {"id": 1, "state": "EXECUTED", "amount": "100.00"},
        {"id": 2, "state": "CANCELED", "amount": "200.00"},
    ]
    with patch("pandas.read_csv", return_value=mock_df):
        result = read_transactions_from_csv(csv_file)
        assert isinstance(result, list)
        assert len(result) == 2
        assert result[0]["id"] == 1


def test_read_transactions_from_csv_file_not_found(csv_file: str):
    """Тест обработки отсутствующего CSV файла"""
    with patch("pandas.read_csv", side_effect=FileNotFoundError):
        with pytest.raises(FileNotFoundError) as exc_info:
            read_transactions_from_csv(csv_file)

        assert f"Файл '{csv_file}' не найден." in str(exc_info.value)


def test_read_transactions_from_csv_general_exception(csv_file: str):
    """Тест обработки общей ошибки при чтении CSV"""
    error_msg = "Произвольная ошибка CSV"

    with patch("pandas.read_csv", side_effect=Exception(error_msg)):
        with pytest.raises(Exception) as exc_info:
            read_transactions_from_csv(csv_file)

        assert f"Ошибка при обработке CSV-файла: {error_msg}" in str(exc_info.value)


def test_read_transactions_from_csv_empty_file(csv_file: str, mock_csv_response):
    """Тест чтения пустого CSV файла"""
    mock_df = mock_csv_response
    mock_df.to_dict.return_value = []

    with patch("pandas.read_csv", return_value=mock_df):
        result = read_transactions_from_csv(csv_file)

        assert isinstance(result, list)
        assert len(result) == 0


def test_read_transactions_from_excel_success(xlsx_file: str, mock_xlsx_response):
    """Тест успешного чтения Excel файла"""
    mock_df = mock_xlsx_response
    mock_df.to_dict.return_value = [
        {"id": 1, "state": "EXECUTED", "amount": "100.00"},
        {"id": 2, "state": "CANCELED", "amount": "200.00"},
    ]

    with patch("pandas.read_excel", return_value=mock_df):
        result = read_transactions_from_excel(xlsx_file)

        assert isinstance(result, list)
        assert len(result) == 2
        assert result[0]["id"] == 1


def test_read_transactions_from_excel_file_not_found(xlsx_file: str):
    """Тест обработки отсутствующего Excel файла"""
    with patch("pandas.read_excel", side_effect=FileNotFoundError):
        with pytest.raises(FileNotFoundError) as exc_info:
            read_transactions_from_excel(xlsx_file)

        assert f"Файл '{xlsx_file}' не найден." in str(exc_info.value)


def test_read_transactions_from_excel_general_exception(xlsx_file: str):
    """Тест обработки общей ошибки при чтении Excel"""
    error_msg = "Произвольная ошибка Excel"

    with patch("pandas.read_excel", side_effect=Exception(error_msg)):
        with pytest.raises(Exception) as exc_info:
            read_transactions_from_excel(xlsx_file)

        assert f"Ошибка при обработке Excel-файла: {error_msg}" in str(exc_info.value)


def test_read_transactions_from_excel_empty_file(xlsx_file: str, mock_xlsx_response):
    """Тест чтения пустого Excel файла"""
    mock_df = mock_xlsx_response
    mock_df.to_dict.return_value = []

    with patch("pandas.read_excel", return_value=mock_df):
        result = read_transactions_from_excel(xlsx_file)

        assert isinstance(result, list)
        assert len(result) == 0
