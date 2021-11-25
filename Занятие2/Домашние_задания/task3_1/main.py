# Написать декоратор, который проверяет, что результатом выполнения исходной
# функции, является список.
# Если это не так, то должна генерироваться соответствующая ошибка:
# ```python
# raise TypeError(f"Результатом выполнения функции {fn} должен быть список") ...



def output_type_list(fn):
    def wrapper(*args, **kwargs):
        result = fn(*args, **kwargs)
        if isinstance(result, list):
            print(result)
            return result
        else:
            raise TypeError(f"Результатом выполнения функции {fn} должен быть список")


        return wrapper

    return wrapper


@output_type_list
def return_list(a) -> list:
    return a


@output_type_list
def return_tuple(b) -> str:
    return b


if __name__ == "__main__":
    return_list([1, 2, 3])
    return_tuple("String")
