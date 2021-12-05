
    # with open(filename, "r") as f:# TODO считать содержимое JSON файла
    #     jsn_fl = json.load(f)
    # gen_exr = (jsn_fl[i]["contains_improvement_appeals"] for i in range(len(jsn_fl)))  # TODO записать выражение-генератор возвращающее значение по ключу contains_improvement_appeals
    # # gen_exr = (item["contains_improvement_appeals"] for item in json_data)
    #
    # return sum(gen_exr)

import json


def task():
    filename = "input.json"
    with open(filename, "r") as f:
        json_file = json.load(f)
    gen_ = (i["contains_improvement_appeals"] for i in json_file)
    # gen_ = (json_file[i]["contains_improvement_appeals"] for i in range(len(json_file)))
    answer = sum(gen_)
    return answer

if __name__ == "__main__":
    print(task())





