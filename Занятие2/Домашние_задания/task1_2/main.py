def flatten(list_of_lists: list): #ИСХОДНАЯ ФУНКЦИЯ, ПЕЧАТАЕТ МАТРИЦУ
    for ceil in list_of_lists:
        print(ceil)

def iterator(list_of_lists_2: list): #ИТЕРАТОР (ВЫРАЖЕНИЕ-ГЕНЕРАТОР, ПЕРЕБИРАЮЩИЙ ЯЧЕЙКИ
    iter_ = (j for i in (list_of_lists_2) for j in i)
    straight_list = list(iter_)
    return straight_list

if __name__ == "__main__":
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    flatten(matrix)
    a = iterator(matrix)
    print(f"""Ответ: 
    {a:<0}""") #fixme почему не получается убрать отступ?

    # for ceil in flatten(matrix):
    #     print(ceil)
# Написать итератор, который будет список списков «вытягивать» в одномерный список.
# И итерироваться сразу по ячейкам, а не строкам, как это обычно устроено


