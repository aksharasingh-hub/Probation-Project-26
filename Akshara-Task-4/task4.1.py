import pandas as pd
import numpy as np
A = pd.Series(np.random.randint(1, 101, size=10))
print("The Series:",A)
print("First 5 elements:",A.head(5))
print("Last 5 elements:",A.tail(5))
print("Maximum value:", A.max())
print("Minimum value:", A.min())
print("Mean of the series:", A.mean())
A_list = A.tolist()
print("Series as a Python list:",A_list)
