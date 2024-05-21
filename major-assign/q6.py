import math

from data import *
from intro.variance import covariance
from q4 import mean


def variance(marks):
    x_mean = mean(marks)
    return sum(pow(xi - x_mean, 2) for xi in marks)


def standard_deviation(marks):
    return math.sqrt(variance(marks))


def correlation(marks1, marks2):
    std_deviation_x = standard_deviation(marks1)
    std_deviation_y = standard_deviation(marks2)
    if std_deviation_x > 0 and std_deviation_y > 0:
        return covariance(marks1, marks2) / (std_deviation_x * std_deviation_y)
    else:
        return 0


print(f"{correlation(cs_marks, maths_marks) = }")
