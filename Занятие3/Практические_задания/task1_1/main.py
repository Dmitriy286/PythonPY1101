def task():
    filename = r"C:\Users\dmishi\PycharmProjects\PythonPY1101\Занятие3\Практические_задания\task1_2\output.txt"
    with open(filename, encoding="utf-8") as f:  # менеджер контекста открывает файл в режиме чтения в текстовом формате "rt"
        for line in f:  # файл является итератором, который построчно возвращает свое содержимое
            line = line.strip()
            # TODO c помощью метода строки strip очистить строку от непечатыемых символов
            print(line)


if __name__ == "__main__":
    task()
