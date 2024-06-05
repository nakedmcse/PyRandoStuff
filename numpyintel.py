# Numpy on intel
import numpy as np
import time

x = np.array([i for i in range(0, 100000000)], dtype=np.uint32)
y = np.array([i for i in range(0, 100000000)], dtype=np.uint32)

start = time.perf_counter()
z = x * y
end = time.perf_counter()

print(z[567])
print(f"Completed in {(end-start)*1000} ms")
