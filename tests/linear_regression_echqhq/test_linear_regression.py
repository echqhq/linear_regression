import numpy as np
from linear_regression_echqhq import linear_regression


class TestFindParams(object):
    def test_small(self):
        y = np.array([[1], [2], [3]])
        x = np.array([[2.01], [3.99], [6.03]])
        b = linear_regression.find_params(y, x)
        print(b)
        assert -0.1 <= b[0, 0] <= 0.1
        assert 0.4 <= b[1, 0] <= 0.6
