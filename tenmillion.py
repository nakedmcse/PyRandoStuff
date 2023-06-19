#Count to 10 million ten times
import time
import numpy as np

print("Starting 10 million x10 count...")
start_time = time.time()
c = np.zeros(10,dtype=np.int64)
c += 10000000
end_time = time.time()

print(c)
elapsed = end_time - start_time
print(f"Elapsed Time: {elapsed:.8f} seconds")
print()
print()