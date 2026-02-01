from typing import Union


def get_valid(*args: Union[int, str]) -> Union[int, str, None]:
    """Функция, которая может принимать и числа, и строки"""
    while True:
        user_input = input(f"Введите {args} или 'стоп': ").strip()

        if user_input.lower() == "стоп":
            return None

        # Сначала проверяем, является ли ввод строкой из args
        if user_input in args:
            return user_input

        # Если нет, пробуем как число
        try:
            number = int(user_input)
            if number in args:
                return number
        except ValueError:
            pass

        print(f"Допустимые значения: {args} или 'стоп'")
