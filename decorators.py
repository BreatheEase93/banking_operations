def log(filename=None):
    """Декоратор, который будет автоматически логироет начало и конец выполнения функции,
    а также ее результаты или возникшие ошибки.
     Декоратор должен принимать необязательный аргумент filename, который определяет, куда будут записываться логи"""

    def my_decorator(func):
        def wrapper(*args, **kwargs):
            try:
                result = func(*args, **kwargs)
                message = f"Функция: {func.__name__}. Результат: {result}."
            except Exception as e:
                message = f"Функция: {func.__name__}. Ошибка: {type(e).__name__} - {e}. Inputs: {args}, {kwargs}"
                result = message
            if filename:
                with open(filename, "a", encoding="utf-8") as f:
                    f.write(message + "\n")
            else:
                print(message)
            return result

        return wrapper

    return my_decorator
