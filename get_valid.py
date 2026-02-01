from typing import Union


def get_valid(*args: Union[int, str]) -> Union[int, str, None]:
    """Функция, которая может принимать числа и строки"""
    while True:
        user_input = input(f"Введите {args} или 'стоп': ").strip().lower()
        if user_input.lower() == "стоп":
            return None
        if user_input in args:
            return user_input
        try:
            number = int(user_input)
            if number in args:
                return number
        except ValueError:
            pass

        print(f"Допустимые значения: {args} или 'стоп'")
