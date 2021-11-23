OUTPUT_FILE = "output.txt"

def task():
    with open(OUTPUT_FILE, "w") as f:
        # for number in range(1, 11):
        str_ = (str(number ** 2) for number in range(1, 11))
        f.write(",".join(str_))


if __name__ == "__main__":
    task()

    with open(OUTPUT_FILE, "r") as f:
        line = next(f)
        line_1 = line.split(",")
        print(line_1)
        str_ = (i for i in line_1)
        print(str_)
        print(next(str_))
        print(next(str_))
        print(next(str_))

        str_2 = ",".join(str_)
        print(str_2)