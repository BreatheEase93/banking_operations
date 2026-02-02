from unittest.mock import patch

from get_valid import get_valid


def test_get_valid_compact():
    """Тесты валидации ввода в компактном стиле"""
    with patch("builtins.input", return_value="да"):
        assert get_valid("да", "нет") == "да"
    with patch("builtins.input", return_value="42"):
        assert get_valid(42, 100) == 42
    with patch("builtins.input", return_value="стоп"):
        assert get_valid(1, 2, 3) is None

    with patch("builtins.input", side_effect=["ошибка", "правильно"]), patch("builtins.print"):
        assert get_valid("правильно", "верно") == "правильно"

    with patch("builtins.input", side_effect=["ошибка1", "ошибка2", "42"]), patch("builtins.print"):
        assert get_valid(42, 100) == 42

    with patch("builtins.input", return_value="  да  "):
        assert get_valid("да", 42) == "да"

    with patch("builtins.input", return_value="-5"):
        assert get_valid(-5, 10) == -5

    with patch("builtins.input", side_effect=["", " ", "42"]), patch("builtins.print"):
        assert get_valid(42) == 42
