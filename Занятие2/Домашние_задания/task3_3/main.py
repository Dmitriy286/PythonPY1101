# def decorator(fn):
#     def wrapper(*args, **kwargs):
#         iter_or_not = (i for i in args[i])
#         if isinstance(iter_or_not, iter):
#             print("Аргумент - итерируемый объект")
#         else:
#             raise TypeError("Объект <название или номер позиционного аргумента> "
#                             "<значение аргумента> не является итерируемым")
#
# @decorator
# def func_1(a, b, c, d):
#     print(a)
#     print(b)
#     print(c)
#     print(d)
#
# if __name__ == "__main__":
#     func_1([1, 2, 3], [3, 4, 5])


# def func_1(*args, **kwargs):
#     print(args)
#     iter_or_not = (i for i in args)
#     print(next(iter_or_not))
#     print(next(iter_or_not))
#
#     if iter(i):
#         print("Аргумент - итерируемый объект")
#     else:
#         raise TypeError("Объект <название или номер позиционного аргумента> "
#                             "<значение аргумента> не является итерируемым")
# if __name__ == "__main__":
#     for i in range(2):
#         func_1([1, 2, 3], [4, 5, 6])

tuple_ = (1, [4, 5, 6])
# print(tuple_[0])
iter_or_not = (iter(i) for i in tuple_)
print(iter_or_not)
try:
    if iter(next(iter_or_not)):
        print("ok")
except:
    print("no")
# print(next(iter_or_not))
# print(next(iter_or_not))
# if iter(iter_or_not):
#     print("iter")
# iter_or_not = 1
# try:
#     if iter(iter_or_not):
#         print("iter")
# except:
#     print("Not iter")
# if iter(i):
#     print("Аргумент - итерируемый объект")
# else:
#     raise TypeError("Объект <название или номер позиционного аргумента> "
#                             "<значение аргумента> не является итерируемым")