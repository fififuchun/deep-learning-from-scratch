import numpy as np  # type: ignore


def AND(x1, x2):
    x = np.array([x1, x2])
    w = np.array([1, 1])
    b = -1

    # print(np.sum(w * x) + b)
    u = np.sum(w * x) + b

    if u <= 0:
        return 0
    else:
        return 1


def OR(x1, x2):
    x = np.array([x1, x2])
    w = np.array([1, 1])
    b = 0

    u = np.sum(w * x) + b

    if u <= 0:
        return 0
    else:
        return 1


print(AND(0, 0))
print(AND(0, 1))
print(AND(1, 0))
print(AND(1, 1))
print()

print(OR(0, 0))
print(OR(0, 1))
print(OR(1, 0))
print(OR(1, 1))
