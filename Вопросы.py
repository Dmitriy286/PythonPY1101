# 1
def a(x):
    return x[0] + x[1]

def b(y):

    print(max(y, key=a))

if __name__ == "__main__":
    points = [
        (1, 2),
        (5, 6),
        (10, 3),
        (4, 2)
    ]
    b(points)