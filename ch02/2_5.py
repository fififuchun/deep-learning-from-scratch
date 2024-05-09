import numpy as np  # type: ignore


def AND(x1, x2):
    x = np.array([x1, x2])
    w = np.array([1, 1])
    b = -1
    u = np.sum(w * x) + b

    if u <= 0:
        return 0
    else:
        return 1


def NAND(x1, x2):
    x = np.array([x1, x2])
    w = np.array([1, 1])
    b = -2
    u = np.sum(w * x) + b

    if u >= 0:
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


# print(NAND(0, 0))
# print(NAND(0, 1))
# print(NAND(1, 0))
# print(NAND(1, 1))


def XOR(x1, x2):
    y1 = NAND(x1, x2)
    y2 = OR(x1, x2)
    return AND(y1, y2)


print(XOR(0, 0))
print(XOR(0, 1))
print(XOR(1, 0))
print(XOR(1, 1))
