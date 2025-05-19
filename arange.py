import numpy as np
import time
import sys

l = range(1000)
print(sys.getsizeof(1)*len(l))

array = np.arange(1000)
print(array.size*array.itemsize)


SIZE = 10000000

l1 = range(SIZE)
l2 = range(SIZE)


a1 = np.arange(SIZE)
a2 = np.arange(SIZE)

start = time.time()

result = [(x+y) for x,y in zip(l1,l2)]

print("Python list took time: ", (time.time()-start)*1000)

start = time.time()
result = a1+a2

print("Numpy array took time: ",(time.time()-start)*1000)

a3 = np.arange(10)
a4 = np.arange(10,20)
print(a3,a4)
sum = a3+a4
print(sum)

l3 = range(10)
l4 = range(10,20)
print(l3,l4)
sum = [(x+y) for x,y in zip(l3,l4)]
print(sum)