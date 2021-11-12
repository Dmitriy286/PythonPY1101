# def min_word(x):
#     for i in range(len(x)):
#         word_length = len(x[i])
#     return word_length
def task() -> str:
    list_words = [
        "Goldenrod",
        "Purple",
        "Salmon",
        "Turquoise",
        "Cyan"
    ]

    return min(list_words, key=len)  # используй ключевую у функции min, по которой она долна определять минимальный элемент


if __name__ == "__main__":
    print(task())
