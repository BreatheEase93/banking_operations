def log(filename=None):
    def my_decorator(func):
        def wrapper(*args, **kwargs):
            try:
                result = func(*args, **kwargs)
                message = f'Функция: {func.__name__}. Результат: {result}.'
            except Exception as e:
                message  = f'Функция: {func.__name__}. Ошибка: {type(e).__name__} - {e}. Inputs: {args}, {kwargs}'
            if filename:
                with open(filename, 'a', encoding='utf-8') as f:
                    f.write(message + '\n')
            else:
                print(message)
            return message
        return wrapper
    return my_decorator

