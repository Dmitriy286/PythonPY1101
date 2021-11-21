def min_len_check(fn):
    def wrapper(*args, **kwargs):# TODO записать обертку для исходной функции
        if len(*args, **kwargs) < 10:
            raise ValueError("Строка слишком короткая")
        result = fn(*args, **kwargs)
        return result
    return wrapper


@min_len_check # TODO задекорировать функцию
def some_func(str_arg: str):
    print(str_arg)


if __name__ == "__main__":
    some_func("Hello, World!!!")  # всё хорошо

    some_func("Short strrrrrr")  # ValueError("Строка слишком короткая")
