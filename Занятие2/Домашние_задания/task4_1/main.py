def pairwise(iterable): #РЕАЛИЗУЕМ ФУНКЦИЮ PAIRWISE
    # pairwise('ABCDEFG') --> AB BC CD DE EF FG
    a = (i for i in iterable)
    b = (iterable[i+1] for i in range(len(iterable) - 1))
    return zip(a, b)

def task(iterable_1): #С ПОМОЩЬЮ ФУНКЦИИ PAIRWISE ФОРМИРУЕМ КОРТЕЖИ ИЗ КООРДИНАТ ДВУХ СОСЕДНИХ ТОЧЕК
    for pair in pairwise(iterable_1):
        yield pair

def length_main(b): #СУММИРУЕМ ДЛИНУ ОТРЕЗКОВ
    gen_ = (((item[1][0] - item[0][0]) ** 2 + (item[1][1] - item[0][1]) ** 2) ** 0.5 for item in b)
    sum_length = (sum(gen_))
    return sum_length

if __name__ == "__main__":
    pts = [
        (3, 4),
        (4.5, 3),
        (2.1, -1),
        (6.8, -3),
        (1.4, 2.9)
    ]
    a = task(pts)
    answer = length_main(a)
    print(answer)
#fixme
