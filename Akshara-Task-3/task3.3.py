import numpy as np
a1=np.random.randint(1,21,size=10)
a2=np.random.randint(1,21,size=10)
print("First array:",a1)
print ("Second array:",a2)
print("Addition:",np.add(a1,a2))
print("Subtraction:",np.subtract(a1,a2))
print("Multiplication:",np.multiply(a1,a2))
print("Division:",np.divide(a1,a2))
squared=a1**2
print("sqaure of first array:",squared)
print("Dot Product:",np.dot(a1,a2))
print("Sorted second array:",np.sort(a2))