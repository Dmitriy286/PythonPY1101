# import json
#
#
# def task():
#     filename = "input.json"
#     with open(filename) as f:
#         json_data = json.load(f)
#
#     map_iterator = map(lambda item: item["score"] * item["weight"], json_data)
#     return sum(map_iterator)
#
#
# if __name__ == "__main__":
#     result = task()
#     print(f"{result:.3f}")

import json

def task():
    filename = "input.json"
    with open(filename, "r") as f:
        jsn_str = json.load(f)
        iter_ = map(lambda x: x["score"] * x["weight"], jsn_str)
        return sum(iter_)

if __name__ == "__main__":
    # print(task())
    result = task()
    print(f"{result:.3f}")


