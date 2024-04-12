import math

import matplotlib.pyplot as plt
import random


def uniform_pdf(x, a=0, b=1):
    return 1 / (b - a) if a <= x < b else 0


def uniform_cdf(x, a=0, b=1):
    if x <= a:
        return 0
    elif a <= x < b:
        return (x - a) / (b - a)
    else:
        return 1


def normal_pdf(x, std_deviation, mean):
    return 1 / (std_deviation * math.sqrt(2 * math.pi)) * (math.exp(-pow(x - mean, 2) / (2 * pow(std_deviation, 2))))


def bernauli_trail(p):
    return 1 if random.random()<p else 0


def binomial(n, p):
    return sum(bernauli_trail(p) for i in range(n))


x_coords = [x / 200 for x in range(-1000, 1000)]
y_coords = [normal_pdf(x, std_deviation=1, mean=0) for x in x_coords]
plt.plot(x_coords, y_coords)
y_coords = [normal_pdf(x, std_deviation=3, mean=0) for x in x_coords]
plt.plot(x_coords, y_coords)
y_coords = [uniform_pdf(x) for x in x_coords]
plt.plot(x_coords, y_coords)
plt.legend(['Normal PDF', 'Uniform PDF 1', 'Uniform PDF 2'])
plt.show()
