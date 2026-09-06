import numpy as np
B = np.random.randint(1,21,size=(3,3))
print("Array:",B)
print("First row:",B[0])
print("Second column:",B[:,1])
print("Element at position(2,2):",B[2,2])
print("Sub array (first two rows and first two columns):",B[:2,:2])
B[1,1]=99
print("Modified array:",B)