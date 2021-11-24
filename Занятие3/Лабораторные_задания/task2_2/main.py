import json


def task(input_filename: str, output_filename: str) -> None:
    with open(input_file, "r") as inp_f:
        with open(output_file, "w") as out_f:
            json_file = json.load(inp_f)
            json.dump(json_file, out_f, indent=4)# TODO считать содержимое json файл input.json

    ...  # TODO записать содержимое в json файл output.json с отступами


if __name__ == "__main__":
    input_file = "input.json"
    output_file = "output.json"

    task(input_file, output_file)

    with open(output_file) as output_f:
        for line in output_f:
            print(line, end="")
