import numpy as np
'''
grades = np.array([[87, 96, 70],[100, 87, 90],
                    [94, 77, 90],[100, 81,82]])

print(grades.sum())

print(grades.min())

print(grades.max())

print(grades.mean())

print(grades.std())

print(grades.var())

print(grades.mean(axis = 0))
print(grades.mean(axis = 1))

numbers = np.array([1,4,9,16,25,36])

print(np.sqrt(numbers))

grades = np.array([[87, 96, 70],[100, 87, 90],
                    [94, 77, 90],[100, 81,82]])

print(grades[0,1])

print(grades[1])

print(grades[0:2])
print()
print()

print(grades[[1,3]])

print(grades[:,0])


#shallow copies
numbers = np.arange(1,6)
number2 = numbers.view()

#print(number2)

numbers[1]*= 10
#print(number2)

number2[1] /= 10
#print(numbers)

numbers2 = numbers[0:3]

#print(numbers2)

# Deep Copy
numbers2 = numbers.copy()


grades = np.array([[87, 96, 70],[100, 87, 90]])

#print(grades.reshape(1,6))

#print(grades)

grades2 = grades.T
print(grades)
print(grades2)
'''

grades = np.array([[87, 96, 70],[100, 87, 90]])
grades2 = np.array([[94,77,90],[100,81,82]])

h_grades = np.hstack((grades,grades2))

print(h_grades)

print(np.vstack((grades,grades2)))