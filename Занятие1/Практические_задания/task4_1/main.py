from itertools import count


def task():
    iterator_numbers = count(1, 1)  # бесконечный счетчик натуральных чисел, который занимает конечный размер в памяти
    iterator_numbers_1 = count(1, 1)
    print(f"Является ли объект итератором? {iterator_numbers is iter(iterator_numbers)}")  # Итератор
    for _ in range(5):  # распечатать первые 5 натуральных чисел
        print(next(iterator_numbers))  # TODO как получить от итератора следующий объект?

    print("Выполнение некоторого кода ...")

    for _ in range(5):  # распечатать следующие 5 натуральных чисел
        print(next(iterator_numbers))  # TODO как получить от итератора следующий объект?
    print("Идем дальше")
    print(next(iterator_numbers))
    print(next(iterator_numbers))
    print(next(iterator_numbers))
    print(next(iterator_numbers))
    print(next(iterator_numbers))
    print(next(iterator_numbers))
    print(next(iterator_numbers))
    print(next(iterator_numbers))
    print(next(iterator_numbers_1))



if __name__ == "__main__":
    task()
