import os
import tempfile

from decorators import log


# Декоратор без файла - успешное выполнение
def test_log_to_console_success(capsys):
    @log()
    def add(a, b):
        return a + b

    result = add(3, 5)

    captured = capsys.readouterr()
    assert "Функция: add. Результат: 8." in captured.out
    assert result == "Функция: add. Результат: 8."


# Тест 2: Декоратор без файла - ошибка
def test_log_to_console_error(capsys):
    @log()
    def divide(a, b):
        return a / b

    result = divide(10, 0)

    captured = capsys.readouterr()
    assert "Ошибка" in captured.out
    assert "Ошибка" in result


# Тест 3: Декоратор с файлом - успешное выполнение
def test_log_to_file_success():
    with tempfile.NamedTemporaryFile(mode="w", delete=False, suffix=".txt") as tmp:
        tmp_filename = tmp.name

    try:

        @log(filename=tmp_filename)
        def multiply(a, b):
            return a * b

        result = multiply(4, 5)

        assert result == "Функция: multiply. Результат: 20."

        with open(tmp_filename, "r", encoding="utf-8") as f:
            content = f.read()
            assert "Результат" in content
    finally:
        os.unlink(tmp_filename)


# Тест 4: Декоратор с файлом - ошибка
def test_log_to_file_error():
    with tempfile.NamedTemporaryFile(mode="w", delete=False, suffix=".txt") as tmp:
        tmp_filename = tmp.name

    try:

        @log(filename=tmp_filename)
        def raise_error():
            raise ValueError("test error")

        result = raise_error()

        assert "Ошибка" in result

        with open(tmp_filename, "r", encoding="utf-8") as f:
            content = f.read()
            assert "Ошибка" in content
    finally:
        os.unlink(tmp_filename)


# Тест 5: Работа с фикстурой из conftest
def test_log_with_fixture(capsys, by_state):
    @log()
    def count_executed(transactions):
        return len([t for t in transactions if t["state"] == "EXECUTED"])

    result = count_executed(by_state)

    captured = capsys.readouterr()
    assert "Функция: count_executed. Результат: 2." in captured.out
    assert result == "Функция: count_executed. Результат: 2."
