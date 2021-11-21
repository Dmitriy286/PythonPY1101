# for i in "ab":
#     for j in "cdef":
#         print(i, j)
#     # print()

# from string import printable
#
# for b1 in printable:
#     for b2 in printable:
#         for b3 in printable:
#             print(b1, b2, b3)

# for j in range(1, 10):
#     for i in range(1, 11):
#
#         print(f"{i} * {j} = {i * j:_>2}", end="  ")
# #     print()
# k = 0
# for b1 in "tukva":
#     for b2 in "tukva":
#         for b3 in "tukva":
#             for b4 in "tukva":
#                 for b5 in "tukva":
#                     for b6 in "tukva":
#                         rez = b1 + b2 + b3 + b4 + b5 + b6
#                         if rez[0] in "tkv" and rez[-1] in "tkv":
#                             if rez.count("a") + rez.count("u") == 2:
#                                 k += 1
# print(k)

n = 64
def lapi():
    for ra in range(n):
        for ge in range(n):
            if ra * 4 + ge * 2 == 64:
                print(f"кроликов {ra} гусей {ge}")

if __name__ == '__main__':
    lapi()