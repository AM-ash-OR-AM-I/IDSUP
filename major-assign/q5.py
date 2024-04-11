from data import *


def covariance(marks1, marks2):
    n = len(marks1)
    x_mean = sum(marks1) / n
    y_mean = sum(marks2) / n
    return sum((xi - x_mean) * (yi - y_mean) for xi, yi in zip(marks1, marks2)) / (
            n - 1
    )


print(f"{covariance(maths_marks, science_marks) = }")
