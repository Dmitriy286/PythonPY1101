from traceback import print_exc

def pseudo_enumerate(any_sequence):
    index_list = []
    for i in any_sequence: # СОЗДАЕМ СПИСОК ИНДЕКСОВ
        index_ = any_sequence.index(i)
        index_list.append(index_)

    print(index_list) # ПРОВЕРКА, ЧТО МЫ ВЫТАЩИЛИ ТО, ЧТО НУЖНО
    print(any_sequence) # ПРОВЕРКА, ЧТО В ФУНКЦИЮ ПЕРЕДАН НУЖНЫЙ СПИСОК


# может, с iter() ???
    for i, b in iter(zip(index_list, any_sequence)): # С ПОМОЩЬЮ ФУНКЦИИ zip ОБЪЕДИНЯЕМ СПИСКИ ИНДЕКСОВ И ЗНАЧЕНИЙ
        print(i, b)
        # return i, b

def proof():
    list_1 = [1, 2, "d", 4]
    try:
        for index_1, value_1 in pseudo_enumerate(list_1):
            print(index_1, value_1)
    except:
        print_exc()

def enumerate_(): # НАСТОЯЩИЙ ENUMERATE
    list_2 = [5, 6, "s", 7]
    for index_2, value_2 in enumerate(list_2):
        print(index_2, value_2)

if __name__ == "__main__":
    proof()
    print("-" * 20)
    enumerate_()