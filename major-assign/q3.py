# 3. Write a Python program to create a list of 20 vectors by taking student’s Math, Computer Science and Science
# marks. Find the sum of all these 20 vectors. After that, find the average marks for Math, Computer Science and
# Science. Hint: [50,60,73] will be one vector.

from data import students

vectors = [
    [student["Math"], student["Computer Science"], student["Science"]]
    for student in students
]
print(vectors)
