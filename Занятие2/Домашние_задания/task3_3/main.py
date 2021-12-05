def decorator(fn):
    def wrapper(*args, **kwargs):

        for i, j in enumerate(args):
            if iter(item for item in j):

                res = fn(*args, **kwargs)
                return res

            else:
                raise TypeError(f"Объект {i} {j} не является итерируемым")
    return wrapper

@decorator
def func_1(a, b, c, d, e):
    print(a, b, c, d, e)

if __name__ == "__main__":
    func_1(1, [1, 2, 3], [3, 4, 5], key1=3, key2=[7, 8, 9])

    #fixme


