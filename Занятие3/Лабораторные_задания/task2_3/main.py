import json


def task():
    filename = "input.json"
    with open(filename, "r") as f:# TODO считать содержимое JSON файла
        jsn_str = json.load(f)

    return max(jsn_str, key=lambda x: x["score"])  # TODO найти максимальный элемент по ключу score
#fixme как это работает?

if __name__ == "__main__":
    print(task())
