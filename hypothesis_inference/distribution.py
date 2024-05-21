import math
import random
from typing import Tuple

import matplotlib.pyplot as plt


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
    return (
        1
        / (std_deviation * math.sqrt(2 * math.pi))
        * (math.exp(-pow(x - mean, 2) / (2 * pow(std_deviation, 2))))
    )


def normal_cdf(x, mu, sigma):
    return 1 + math.erf((x - mu) / (sigma * math.sqrt(2)))


# def inverse_cdf(p, std_deviation=1, mean=0, tolerance=0.00001):
#     if mu


def bernauli_trail(p):
    return 1 if random.random() < p else 0


def binomial(n, p):
    return sum(bernauli_trail(p) for i in range(n))


# Hypothesis Testing


def normal_approximation_to_binomial(n: int, p: float) -> Tuple[float, float]:
    """
    n -> no. of trials
    p -> probability

    Return mu and sigma corrensponding to binomial(n, p)
    """
    mu = p * n
    sigma = math.sqrt(p * (1 - p) * n)
    return mu, sigma


def normal_probability_above(x, mu, sigma):
    return 1 - normal_cdf(x, mu, sigma)


normal_probability_below = normal_cdf


# opposite of confidence interval
def two_sided_p_value(x: float, mu: float, sigma: float = 1) -> float:
    if x >= mu:
        return 2 * normal_probability_above(x, mu, sigma)
    else:
        return 2 * normal_probability_below(x, mu, sigma)


def normal_probability_between(lo: float, hi: float, mu: float = 0, sigma: float = 1):
    return normal_cdf(hi, mu, sigma) - normal_cdf(lo, mu, sigma)


x_coords = [x / 200 for x in range(-1000, 1000)]
y_coords = [normal_pdf(x, std_deviation=1, mean=0) for x in x_coords]
plt.plot(x_coords, y_coords)
y_coords = [normal_pdf(x, std_deviation=3, mean=0) for x in x_coords]
plt.plot(x_coords, y_coords)
y_coords = [uniform_pdf(x) for x in x_coords]
plt.plot(x_coords, y_coords)
plt.legend(["Normal PDF", "Uniform PDF 1", "Uniform PDF 2"])
plt.show()
