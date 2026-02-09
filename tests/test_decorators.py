import os
import tempfile

from decorators import log


# Тест 1: Успешное выполнение с выводом в консоль
def test_log_to_console_success(capsys):
    @log()
    def add(a, b):
        return a + b

    result = add(3, 5)

    captured = capsys.readouterr()
    assert "Функция: add. Результат: 8." in captured.out
    assert result == 8


# Тест 2: Ошибка с выводом в консоль
def test_log_to_console_error(capsys):
    @log()
    def divide(a, b):
        return a / b

    result = divide(10, 0)

    captured = capsys.readouterr()
    assert "Ошибка" in captured.out
    assert "ZeroDivisionError" in str(result)


# Тест 3: Успешное выполнение с записью в файл
def test_log_to_file_success():
    with tempfile.NamedTemporaryFile(mode="w", delete=False, suffix=".txt") as tmp:
        tmp_filename = tmp.name

    try:

        @log(filename=tmp_filename)
        def multiply(a, b):
            return a * b

        result = multiply(4, 5)

        assert result == 20

        with open(tmp_filename, "r", encoding="utf-8") as f:
            content = f.read()
            assert "Результат: 20." in content
    finally:
        os.unlink(tmp_filename)


# Тест 4: Работа с фикстурой by_state
def test_log_with_fixture(capsys, by_state):
    @log()
    def count_executed(data):
        return len([item for item in data if item["state"] == "EXECUTED"])

    result = count_executed(by_state)

    captured = capsys.readouterr()
    assert "Результат: 2." in captured.out
    assert result == 2
