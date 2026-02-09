import functools
from typing import Any, Callable, Optional, TypeVar, cast

F = TypeVar("F", bound=Callable[..., Any])


def log(filename: Optional[str] = None) -> Callable[[F], F]:
    """Декоратор, который будет автоматически логировать начало и конец выполнения функции,
    а также ее результаты или возникшие ошибки.
    Декоратор должен принимать необязательный аргумент filename, который определяет, куда будут записываться логи"""

    def my_decorator(func: F) -> F:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
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

        return cast(F, wrapper)  # type: ignore

    return my_decorator
