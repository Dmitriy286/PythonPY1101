# def pairwise(iterable):
#     a = (i for i in iterable)
#     b = ()
#     zip(iterable)
#     yield
from itertools import tee

# def pairwise(iterable):
#     # pairwise('ABCDEFG') --> AB BC CD DE EF FG
#
#     a, b = tee(iterable)
#     next(b, None)
#     return zip(a, b)

#
def pairwise(iterable):
    # pairwise('ABCDEFG') --> AB BC CD DE EF FG
    a = (i for i in iterable)
    b = (iterable[i+1] for i in range(len(iterable) - 1))

    return zip(a, b)

def task():
    for pair in pairwise("ABCDEFG"):
        print(pair)


if __name__ == "__main__":
    task()

#fixme
