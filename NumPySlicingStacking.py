import re
import numpy as np
print("Slicing and Indexing")
a = np.array([1,2,3,4,5,6,7,8,9,10])
print(a)
print(a[0:5])  # Slicing
print(a[5:])  # Slicing
print(a[:5])  # Slicing
print(a[::2])  # Slicing
print(a[-1])  # Accessing the last element
print("Multi-dimensional array")
a = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(a)
print(a[1,2])
print(a[0:3, 2]) # Slicing
print(a[0:3,1])
print(a[1:3,0:2])
print(a[-1])
print(a[-1, 0:2])
print("task\n",a[:,1:3])

for row in a:
    print(row)

for cell in a.flat:
    print(cell)

print("task\n",a.flatten())

print("stacking")
b = np.arange(6).reshape(3,2)
c = np.arange(6,12).reshape(3,2)

for row in b:
    print(row) 
print(c)
result = np.vstack((b,c))
print("vstack:\n",result)
result = np.hstack((b,c))
print("hstack:\n",result)
result = np.dstack((b,c))
print("dstack:\n",result)
result = np.column_stack((b,c))
print("column_stack:\n",result)
result = np.row_stack((b,c))
print("row_stack:\n",result)
result = np.concatenate((b,c), axis=0)
print("concatenate:\n",result)



d = np.arange(30).reshape(2,15)
print(d)
result = np.hsplit(d, 3)
print("hsplit:\n",result)
print("first:", result[0])
print("second:", result[1])
print("third:", result[2])

result = np.vsplit(d, 2)
print("vsplit:\n",result)
print("first:", result[0])
print("second:", result[1])

print("Indexing with boolean arrays")

d = np.arange(12).reshape(3,4)
print(d)
result = d > 4
print(result)  # Boolean indexing

print(d[result])  # Boolean indexing
print(d[d > 4])  # Boolean indexing
print(d[d > 4].shape)  # Shape of the result
print(np.mean(d[d > 4]))  # Mean of the result
d[result]=-1
print(d)  # Boolean indexing