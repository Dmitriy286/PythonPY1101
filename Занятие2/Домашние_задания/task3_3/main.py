def decorator(fn):
    def wrapper(*args, **kwargs):
        iter_or_not = (i for i in args)
        return fn()
        else:
        raise TypeError("Объект <название или номер позиционного аргумента> "
                        "<значение аргумента> не является итерируемым")

@decorator
def func_1(a, b, c, d):
    print(a)
    print(b)
    print(c)
    print(d)

if __name__ == "__main__":
    func_1([1, 2, 3], {1, 3, 4}, xy=[4, 5, 6], yx=[6, "d", "a"])
