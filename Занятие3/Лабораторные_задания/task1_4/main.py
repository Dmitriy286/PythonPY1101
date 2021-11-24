INPUT_FILE = "input.txt"
OUTPUT_FILE = "output.txt"


def task():
    with open(INPUT_FILE, "r") as f:
        with open(OUTPUT_FILE, "w") as wf:

            for str_ in map(str.upper, f):




                wf.write(str_)

                # TODO перезаписать содержимое одного файла в другой
                # wf.write(str(map(str.upper, f)))

if __name__ == "__main__":
    task()

    with open(OUTPUT_FILE) as file:
        for line in file:
            print(line, end="")

