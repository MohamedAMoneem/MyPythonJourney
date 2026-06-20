import numpy as np
import time
import sys
amount = 100000

list = list(range(amount))

start = time.time()
list_result = [n + n for n in list]
print(f"time: {time.time() - start}")

array = np.arange(amount)

start = time.time()
array_result = array + array
print(f"time: {time.time() - start}")