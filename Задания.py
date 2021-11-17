# def table():
#     tab_ = [
#         [i * j for j in range(1, 10)]
#         for i in range(1, 10)
#     ]
#     print(tab_)
#
#     for row in range(len(tab_)):
#         for col in range(len(tab_[row])):
#             ceil = tab_[row][col]
#
#             print(f"{ceil:>2}", end=" ")
#         print()
#
# if __name__ == '__main__':
#     table()


#
# def table():
#
#     for row in range(10):
#         for col in range(10):
#             print(f"{row * col:>2}", end=" ")
#         print()
#
# if __name__ == '__main__':
#     table()


def func(n):
    local_n = n
    dict_ = {}
    list_ = [64, 32, 16, 8, 4, 2, 1]
    for i in list_:
        m = local_n // i
        local_n = local_n % i
        if m != 0:
            dict_[f"Купюра {i}"] = m
    return dict_

if __name__ == '__main__':
    print(func(127))

dict_1 = {f"Купюра {2 ** i}": 0 for i in range(6, -1, -1)}
print(dict_1)

# У гусей и кроликов вместе 64 лапы.
# Сколько могло быть кроликов и гусей (указать все сочетания, которые возможны)?
n = 64
a = 4
b = 2
# ra =
# ge =
# ge * 2 + ra * 4 = 64

def lapi():
    for ra in range(int(64/4 + 1)):
        for ge in range (int(64/2 + 1)):
            ge = (64 - 4 * ra) // 2
        print(ra, ge)

if __name__ == '__main__':
    lapi()

# def table():
#     tab_ = [
#         [i * j for j in range(1, 10)]
#         for i in range(1, 10)
#     ]
#     print(tab_)
#
#     for row in range(len(tab_)):
#         for col in range(len(tab_[row])):
#             ceil = tab_[row][col]
#
#             print(f"{ceil:>2}", end=" ")
#         print()
#
# if __name__ == '__main__':
#     table()