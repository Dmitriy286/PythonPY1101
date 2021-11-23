def task(camel_case_str: str) -> str:
    char = filter(str.islower, camel_case_str)
    # print(next(char))
    # print(next(char))
    # print(next(char))
    # print(next(char))


    return "".join(char)  # TODO отфильтровать только буквы нижнего регистра


if __name__ == "__main__":
    word = "AbCdEfGh"
    print(task(word))
