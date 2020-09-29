import numpy as np

integers = np.array([1,2,3])

'''
print(integers)

print(type(integers))
'''

integers = np.array([[1,2,3],[4,5,6]])

print(integers.dtype)

print(integers.ndim)

print(integers.shape) # Number of dimensions 

print(integers.size) # Number of elements in the array

print(integers.itemsize)

for row in integers:
    print(row)
    print()

    for col in row:
        print(col, end = ' ')
    print()

for i in integers.flat:
    print(i, end = ' ')

print(np.zeros(5)) # Create an array of 5 zeros

print(np.ones(5)) # Create an array of 5 ones
print()
print()
print()

array1 = np.ones((2,4),dtype = int)

print(array1)

array2 = np.full((3,5),13)

print(array2)

print(np.arange(5))

print(np.arange(5,10))

print(np.arange(10,1,-2))

print(np.linspace(0.0,1.0,num = 5))

array1 = np.arange(1,21)
print(array1)

array2 = array1.reshape(4,5)
print(array2)

array3 = np.arange(1,100001).reshape(4,25000)
print(array3)

array4 = np.arange(1,100001).reshape(100,1000)
print(array4)

numbers = np.arange(1,6)

print(numbers*2)
print(numbers)

numbers *=10
print(numbers)

print(numbers ** 3)

numbers = np.arange(1,6)

print(numbers ** 2)

numbers *= 2

print(numbers >=13)

numbers2 = np.arange(5,10)

print(numbers2>numbers)

print(numbers == numbers2)