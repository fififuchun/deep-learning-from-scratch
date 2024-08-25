import sys, os
import numpy as np  # type: ignore
import pickle

sys.path.append(os.pardir)
from dataset.mnist import load_mnist

(x_train, t_train), (x_test, t_test) = load_mnist(
    flatten=True, normalize=False, one_hot_label=False
)

print(x_train.shape)
print(t_train.shape)
print(x_test.shape)
print(t_test.shape)

# print(1 + 2)
