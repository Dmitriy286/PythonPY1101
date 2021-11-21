from string import ascii_lowercase, ascii_uppercase, digits
import random

def pass_(password, n):

    rez = random.sample(password, n)
    rez_2 = "".join(rez)
    yield rez_2
if __name__ == "__main__":

    print(ascii_lowercase, type(ascii_lowercase))
    print(ascii_uppercase)
    print(digits, type(digits))
    chars = ascii_lowercase + ascii_uppercase + digits
    for _ in range(20):
        print(next(pass_(chars, 8)))
