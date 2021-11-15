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

def foo(bar=[]):
    bar.append("baz")
    return bar

print(foo())
print(foo())
print(foo())

def foo_2(bar=None):
    if bar is None:
        bar = []
    bar.append("baz")
    return bar

print(foo_2())
print(foo_2())
print(foo_2())

try:
    l = ["a", "b"]
    m = int(l[2])
    print(m)
except (ValueError, IndexError) as e:
    print("Some except")
    print(e)
    
prices = {
    "apple": 80,
    "orange": 100,
    "pear": 70
}

print(prices)

for fruit in prices:
    print(fruit)

for fruit in prices:
    print(prices[fruit])

for item in prices.items():
    print(item)

for fruit, price in prices.items():
    print(fruit, price)

for fruit, price in prices.items():
    print("Фрукт", fruit, "cтоит = ", price)

usd_to_rub = 72
for fruit, price in prices.items():
    print(f"Фрукт {fruit} cтоит = {price * usd_to_rub}")

s1 = "a"
s2 = "ab"
s3 = "abc"
s4 = "abcd"

print(f"{s1:_>4}")
print(f"{s2:_>4}")
print(f"{s3:_<4}")
print(f"{s4:_<4}")

width = 10
precision = 3
value = 12.34567
print(f"result: {value:0{width}.{precision}f}")

value = 12.34567
print(f"{value:.2f}")