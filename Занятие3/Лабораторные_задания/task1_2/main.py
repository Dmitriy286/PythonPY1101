OUTPUT_FILE = "output.txt"


def task():
    with open(OUTPUT_FILE, "w") as f: # TODO записать лесенку в файл
        for line in range(1, 11):
            f.write(f"{'*' * line:>10}\n")

            # f.write(f"{line * '*':>10}\n")


def print_():
    with open(OUTPUT_FILE, "r") as f:
        for line in f:
            print(line, end="")

if __name__ == "__main__":
    task()
    print_()






















    #
    # with open(OUTPUT_FILE) as file:
    #     for line in file:
    #         print(line, end="")
