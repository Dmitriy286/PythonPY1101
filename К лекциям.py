# a = 34
# print(isinstance(a, (int, list)))
# print(isinstance(a, int))
#
# b = None
# print(b is None)

def add_func(a: int, b: int) -> int:
    if not isinstance(a, int):
        raise ValueError("Only int")
    if not isinstance(b, int):
        raise ValueError("Only int")
    return a + b
func_ = add_func(1, 2)
print(func_, type(func_))


dict_ = {
    "a": 1,
    "b": 2,
    "c": 3
}
print(dict_)

list_ = [2, 3, 4, 5, 6]
gen_dict = {i: i ** 2 for i in list_}
print(gen_dict)

list_1 = [2, 3, 4, 5, 6]
gen_dict_2 = {i+1: b ** 2 for i, b in enumerate(list_1)}
print(gen_dict_2)
print(dict_["b"])
dict_["b"] = 1000
print(dict_)
dict_["a", "c"] = 2000, 3000
print(dict_)
print(dict_["a"])
print(dict_["a", "c"])
dict_[1] = 7000
print(dict_)