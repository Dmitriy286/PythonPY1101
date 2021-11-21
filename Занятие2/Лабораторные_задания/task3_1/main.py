def positive_check(fn):

    def wrapper(arg):
        if arg > 0:# TODO написать проверку положительности аргумента arg
            result = fn(arg)

            return result
        else:
            raise ValueError("Аргумент функции не является положительным числом")

    return wrapper


@positive_check
# # TODO задекорировать функцию
def some_func_1(a):
    print(a)
@positive_check
def some_func_2(b):
    print(b)

# some_func_1 = positive_check(some_func_1)
# some_func_2 = positive_check(some_func_2)


if __name__ == "__main__":

    some_func_1(5)  # всё хорошо

    some_func_2(-5)  # должна быть вызвана ошибка ValueError
