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


# 1 лабораторное задание 1_3
# 2 лабораторное задание 2_1 - как происходит итерирование? Как склеивает методом join? Где там цикл?
# 3:
def try_except():
    # while not int_.isdigit():
    while True:
        try:
            input_ = input("Enter number: ")
            int_ = int(input_)
        except ValueError: # или Exception
            print("Not number")
        else:
            print(int_)
            return int_
        finally:
            print("Test")
        # if str(input_).isdigit():
        if not ValueError: # - ВОТ ЭТО ВЕРНО?????
            break

    print("Test_2")
try_except()

print("-" * 20)
print("Next code")
print("-" * 20)

# 4 что это?:
dict_ = {
    "a": 1,
    "b": 2,
    "c": 3
}
print(dict_)
print(dict_["b"])
dict_["b"] = 1000
print(dict_)
dict_["a", "c"] = 2000, 3000
print(dict_)
print(dict_["a"])
print(dict_["a", "c"])

# 5 псевдо-enumerate (задание 1_1 в Д/З)