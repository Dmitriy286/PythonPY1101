import json

#
# def task():
#     filename = "input.json"
#     with open(filename) as f:
#         json_data = json.load(f)
#
#     return sorted(json_data, key=lambda x: x["length"]) # TODO отсортировать список словарей
#
#
# if __name__ == "__main__":
#     data = task()
#     print(json.dumps(data, indent=4))
#
#     # TODO дополнительно записать отсортированный список в JSON файл

def task():
    filename = "input.json"
    with open(filename, "r") as f:
        json_data = json.load(f)
    sorted_dict = sorted(json_data, key=lambda x: x["length"])
    return sorted_dict

def task_2(jsndata):
    filename_2 = "output.txt"
    with open(filename_2, "w") as f_2:
        json.dump(jsndata, f_2, indent=4)

if __name__ == "__main__":
    data = task()
    task_2(data)
    print(json.dumps(data, indent=4))

#fixme что такое indent? Как он работает? Как понять, что его надо использовать?