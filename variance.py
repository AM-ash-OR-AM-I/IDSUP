import matplotlib.pyplot as plt
import numpy as np


def dot_product(v, w):
    """Computes v_1 * w_1 + ... + v_n * w_n"""
    return sum(v_i * w_i for v_i, w_i in zip(v, w))


def sum_of_squares(v):
    """Computes the sum of squared elements in v"""
    return dot_product(v, v)


def deviation_product(x):
    """Translate x by subtracting its mean (so the result has mean 0)"""
    x_bar = sum(x) / len(x)
    return [xi - x_bar for xi in x]


def variance(v):
    """Computes the variance of v"""
    n = len(v)
    deviations = deviation_product(v)
    return sum_of_squares(deviations) / (n - 1)


def standard_deviation(x):
    return pow(variance(x), 0.5)


def covariance(x, y):
    n = len(x)
    x_mean = sum(x) / n
    y_mean = sum(y) / n
    return sum((xi - x_mean) * (yi - y_mean) for xi, yi in zip(x, y)) / (n - 1)


def correlation(x, y):
    stdev_x = standard_deviation(x)
    stdev_y = standard_deviation(y)
    if stdev_x > 0 and stdev_y > 0:
        return covariance(x, y) / (stdev_x * stdev_y)
    else:
        return 0


# Generate random arrays
np.random.seed(0)
x = np.random.randint(0, 100, 100)
np.random.seed(1)
y = np.random.randint(0, 100, 100)

plt.plot(x, y, marker="o")
plt.show()

print("Variance of x: ", variance(x))
print("Standard deviation of x: ", standard_deviation(x))
print("Variance of y: ", variance(y))
print("Standard deviation of y: ", standard_deviation(y))
print("Covariance of x and y: ", covariance(x, y))
print("Correlation of x and y: ", correlation(x, y))
