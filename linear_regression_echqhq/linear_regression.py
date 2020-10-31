import numpy as np


def find_params(y, x):
    ones = np.ones((x.shape[0], 1))
    x = np.concatenate([ones, x], axis=1)
    b = np.linalg.inv(x.T @ x) @ x.T @ y
    return b