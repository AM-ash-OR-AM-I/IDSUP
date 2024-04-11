# 1. Write a Python program to group the student ids corresponding to the following Science mark.
# • less or equal to 30.
# • between 30 and 70.
# • more than 70.
from collections import defaultdict

from data import students

groups = defaultdict(list)
for student in students:
    student_id, science_marks = student["student id"], student["Science"]
    if science_marks <= 30:
        groups["<30"].append(student_id)
    elif 30 < science_marks <= 70:
        groups["30-70"].append(student_id)
    else:
        groups["70+"].append(student_id)

print(dict(groups))
