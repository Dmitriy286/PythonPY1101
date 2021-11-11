# from itertools import count
# def task_1():
#     count_1 = count(1, 1)
#     count_2 = count(1, 1)
#     for _ in range(5):
#         print(next(count_1))
#         print(next(count_2))
#
# def task_2():
#     count_1 = count(1, 1)
#     count_2 = count(1, 1)
#     for _ in range(5):
#         print(next(count_1))
#         print(next(count_2))
#
# def task_3():
#     count_1 = count(1, 1)
#     count_2 = count_1
#     for _ in range(2):
#         print(next(count_1))
#         print(next(count_2))
#
# for _ in range(5):
#     print(next(count_1))
#     print(next(count_2))
#
#     print(count_1 is count_2)

list_ = [1, 2, 3]

def endless_list():
    for value in list_:
        print(value)
        list_.append(len(list_) + 1)
        if value > 15:
            break

def endless_tuple():
    tuple_ = (1, 2, 3)

    for value in tuple_:
        print(value)
        tuple_ += (len(tuple_),)

    print(tuple_)

if __name__ == '__main__':
    endless_tuple()