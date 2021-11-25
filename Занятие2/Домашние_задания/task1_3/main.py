
#     """
# Написать функцию-генератор, которая будет разбить список длиной N на подсписки длиной k.
# Длина k задается динамически.
#
# Функция должна быть выть оформлена в виде "ленивых" вычислений, а именно,
# что подсписки генерируются не все сразу, а вычисляются раз за разом.
#
# Например:
# ```text
# k = 3
# [1, 2, 3, 4, 5, 6, 7, 8] -> [[1, 2, 3], [4, 5, 6], [7, 8]]
# ```
#
# <div class="hint">
#   Общая формула подсписков
#
#     [
#         [k * 0: k * 1],
#         [k * 1: k * 2],
#         [k * 2: k * 3],
#         ...
#         [k * i: k * (i + 1)]
#     ]
#     """

def sub_list_gen(src_list: list, k: int):
    a = len(src_list) // k
    b = len(src_list) % k
    if b == 0:
        number_of_iterations = a
    else:
        number_of_iterations = a + 1

    for i in range(number_of_iterations):
        new_list = src_list[k*i:k*(i+1)]
        yield new_list

if __name__ == "__main__":
    for sub_list in sub_list_gen([1, 2, 3, 4, 5, 6, 7, 8], 3):
        print(sub_list)
