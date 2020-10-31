from linear_regression_echqhq import linear_regression
import linear_regression_echqhq
import numpy as np

y = np.array([[1], [2], [3]])
x = np.array([[2.01], [3.99], [6.03]])
b = linear_regression_echqhq.linear_regression.find_params(y, x)
# b = linear_regression.find_params(y, x)
print(b)