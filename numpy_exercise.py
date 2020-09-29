import numpy as np

grades = np.random.randint(60,101,12).reshape(3,4)

print(grades)
print("All grades",grades.mean())
print("AVG by each test",grades.mean(axis = 0))
print("AVG by each student", grades.mean(axis = 1))
