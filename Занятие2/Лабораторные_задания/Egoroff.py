def decorator(fn):

    def wrapper(*args, **kwargs):
        print("Function start")
        fn(*args, **kwargs)
        print("Function end")

        # return rez
    return wrapper

@decorator
def func_1(a, b):
    print(a + b)

@decorator
def func_2(a, b, c):
    print(a * b * c)

func_1(5, 6)

func_2(3, 4, 7)

