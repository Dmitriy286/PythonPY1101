def decorator(fn):
    def wraper(*args):
        if type(*args) == int:
            print("Positional argument is integer")
        else:
            print("Positional argument is not integer")
        fn(*args)
    return wraper

@decorator
def print_(a):
    print(a)

@decorator
def print_1(b):
    print(b)

if __name__ == "__main__":
    print_(8)
    print_1("str")