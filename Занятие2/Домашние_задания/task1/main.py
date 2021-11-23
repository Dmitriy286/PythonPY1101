from itertools import count

def generator(a, b):
    yield a
    while True:
        a *= b
        yield a

if __name__ == "__main__":
    gen = generator(10, 2)
    for i in range(10):
        print(next(gen))
        # if i > 100000:
        #     break
