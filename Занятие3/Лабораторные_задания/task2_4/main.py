import json


def task():
    filename = "input.json"
    with open(filename, "r") as f:# TODO считать содержимое JSON файла
        jsn_fl = json.load(f)
    gen_exr = (jsn_fl[i]["contains_improvement_appeals"] for i in range(len(jsn_fl)))  # TODO записать выражение-генератор возвращающее значение по ключу contains_improvement_appeals
    # gen_exr = (item["contains_improvement_appeals"] for item in json_data)
    #fixme
    return sum(gen_exr)



if __name__ == "__main__":
    print(task())
