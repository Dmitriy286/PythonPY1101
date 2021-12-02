def decorator(fn):
    def wrapper(*args, **kwargs):
        result = fn(*args, **kwargs)
        print(result)
        iter_or_not = (i for i in args)
        try:
            iter(next(iter_or_not))
            print("Аргумент - итерируемый объект")

        except:
            raise TypeError("Объект <название или номер позиционного аргумента> "
                            "<значение аргумента> не является итерируемым")
    return wrapper

@decorator
def func_1(a, b, c):
    print(a, b, c)

if __name__ == "__main__":
    func_1(1, [1, 2, 3], [3, 4, 5])
    print(type(func_1))

