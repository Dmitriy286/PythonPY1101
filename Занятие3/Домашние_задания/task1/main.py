import json


def task_1():
    with open(filename_1, "r") as f_1:
        jsn_list_1 = json.load(f_1)
    return(jsn_list_1)


def task_2():
    with open(filename_2, "r") as f_2:
        jsn_list_2 = json.load(f_2)
    return(jsn_list_2)


if __name__ == "__main__":
    filename_1 = "1.txt"
    filename_2 = "2.txt"
    list_1 = list(task_1())
    list_2 = list(task_2())
    print(list_1, type(list_1))
    print(list_2, type(list_2))
    list_3 = list_1 + list_2
    print(list_3)
    print(task_1(), type(task_1))
    print(task_2(), type(task_2))

# fixme верно ли понято задание?