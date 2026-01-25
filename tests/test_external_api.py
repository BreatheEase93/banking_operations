from unittest.mock import patch
from external_api import withdrawal_of_the_amount
import requests
import pytest


class TestWithdrawalOfTheAmount:

    def test_withdrawal_rub_currency(self, by_transactions_1):
        """Тест для транзакции в рублях"""
        transaction = by_transactions_1[0]
        result = withdrawal_of_the_amount(transaction)
        assert result == 43318.34

    def test_withdrawal_usd_currency_success(self, by_transactions_2, mock_api_response):
        """Тест для транзакции в USD с успешным ответом от API"""
        # Arrange
        transaction = by_transactions_2[0]
        mock_data = {"rates": {"RUB": 75.5}, "base": "USD"}
        mock_api_response.json.return_value = mock_data

        expected_amount = 9824.07 * 75.5

        # Act & Assert
        with patch('requests.get', return_value=mock_api_response):
            with patch.dict('os.environ', {'API_KEY': 'test_key'}):
                result = withdrawal_of_the_amount(transaction)

        # Assert
        assert result == expected_amount
        mock_api_response.raise_for_status.assert_called_once()

    def test_withdrawal_api_connection_error(self, by_transactions_2, mock_api_response):
        """Тест для обработки ошибки соединения с API"""
        # Arrange
        transaction = by_transactions_2[0]

        # Act & Assert
        with patch('requests.get', side_effect=requests.exceptions.ConnectionError):
            with patch.dict('os.environ', {'API_KEY': 'test_key'}):
                result = withdrawal_of_the_amount(transaction)

        # Assert
        assert result == 0

    def test_withdrawal_api_timeout_error(self, by_transactions_2, mock_api_response):
        """Тест для обработки таймаута при запросе к API"""
        # Arrange
        transaction = by_transactions_2[0]

        # Act & Assert
        with patch('requests.get', side_effect=requests.exceptions.Timeout):
            with patch.dict('os.environ', {'API_KEY': 'test_key'}):
                result = withdrawal_of_the_amount(transaction)

        # Assert
        assert result == 0

    def test_withdrawal_api_http_error(self, by_transactions_2, mock_api_response):
        """Тест для обработки HTTP ошибки от API"""
        # Arrange
        transaction = by_transactions_2[0]
        mock_api_response.raise_for_status.side_effect = requests.exceptions.HTTPError("404 Not Found")

        # Act & Assert
        with patch('requests.get', return_value=mock_api_response):
            with patch.dict('os.environ', {'API_KEY': 'test_key'}):
                result = withdrawal_of_the_amount(transaction)

        # Assert
        assert result == 0

    def test_withdrawal_api_unknown_error(self, by_transactions_2, mock_api_response):
        """Тест для обработки неизвестной ошибки"""
        # Arrange
        transaction = by_transactions_2[0]

        # Act & Assert
        with patch('requests.get', side_effect=Exception("Unknown error")):
            with patch.dict('os.environ', {'API_KEY': 'test_key'}):
                result = withdrawal_of_the_amount(transaction)

        # Assert
        assert result == 0

    def test_withdrawal_invalid_structure(self, invalid_transactions):
        """Тест для транзакций с некорректной структурой"""
        for transaction in invalid_transactions:
            # Act & Assert
            with pytest.raises(KeyError, TypeError):
                withdrawal_of_the_amount(transaction)

    def test_withdrawal_api_key_not_set(self, by_transactions_2):
        """Тест когда API ключ не установлен"""
        # Arrange
        transaction = by_transactions_2[0]

        # Act & Assert
        with patch.dict('os.environ', {}, clear=True):
            # Так как у нас есть блок try-except, функция вернет 0
            result = withdrawal_of_the_amount(transaction)

        # Assert
        assert result == 0

    def test_withdrawal_api_invalid_response_structure(self, by_transactions_2, mock_api_response):
        """Тест для некорректной структуры ответа от API"""
        # Arrange
        transaction = by_transactions_2[0]
        mock_api_response.json.return_value = {"error": "Invalid request"}  # Нет ключа 'rates'

        # Act & Assert
        with patch('requests.get', return_value=mock_api_response):
            with patch.dict('os.environ', {'API_KEY': 'test_key'}):
                result = withdrawal_of_the_amount(transaction)

        # Assert
        assert result == 0