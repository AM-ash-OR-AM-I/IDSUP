# 2. Create a line chart for student ids and Computer Science marks. Student id on the x-axis and Computer Science
# mark on the y-axis.

from matplotlib import pyplot as plt

from data import students

students_ids = [student["student id"] for student in students]
student_marks = [student["Computer Science"] for student in students]

plt.title("Student Marks CS")
plt.legend(["Student", "CS Marks"])
plt.plot(students_ids, student_marks)
plt.show()
