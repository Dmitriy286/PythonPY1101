def print_args(*args):
    print(type(args), args)


def print_kwargs(**kwargs):
    print(type(kwargs), kwargs)
    dict_ = kwargs
    print(dict_)
    dict_["test3"] = 4
    print(dict_)

def print_args_kwargs(*args, **kwargs):
    for index, arg in enumerate(args):
        print(f"Позиционный аргумент {index + 1}: {arg}")

    for key, kwarg in kwargs.items():
        print(f"Именованный аргумент {key}: {kwarg}")


if __name__ == "__main__":
    print_args(1, 2, "str")
    print_kwargs(test = "1", test2 = 3)

    print_args_kwargs(1, 2, 3, test = "1", test2 = 3)
