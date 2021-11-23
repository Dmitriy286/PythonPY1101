def decorator(fn):
    def wraper(*args):
        print(args)

        # if type(*args) == int:  # isinstance(obj, int)
        #     print("Positional argument is integer")
        # else:
        #     print("Positional argument is not integer")
        res = fn(*args)
        return res
    return wraper

# @decorator
def print_(*a):
    print(a)
    for arg in a:
        print(arg)

# @decorator
def print_1(b):
    print(b)

if __name__ == "__main__":
    tuple_ = (8, 10, 6)

    print_(tuple_)  # print_((8, 10, 6))
    print_(*tuple_)  # print_(8, 10, 6)

    print_1("str")