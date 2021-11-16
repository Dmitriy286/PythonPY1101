def task(numbers: list) -> int:
    gen_exp = (i ** 2 for i in numbers)
    return sum(gen_exp)

def task_2():
    gen_exp_2 = (i ** 2 for i in range(1, 11))
    return sum(gen_exp_2)

if __name__ == "__main__":
    list_numbers = [i for i in range(1, 11)]  # list(range(1, 11))
    print(task(list_numbers))
    print(task_2())
