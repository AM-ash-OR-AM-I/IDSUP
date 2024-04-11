from collections import Counter

from data import *


def mean(marks):
    return sum(marks) / len(marks)


def median(marks):
    marks = sorted(marks)
    n = len(marks)
    if n % 2 == 0:
        return (marks[(n - 1) // 2] + marks[n // 2]) / 2
    else:
        return marks[n // 2]


def mode(marks):
    ctr = Counter(marks)
    return max(ctr.items(), key=lambda x: x[1])[0]


print(f"{mean(cs_marks) = }, {median(cs_marks) = }, {mode(cs_marks) = }")
