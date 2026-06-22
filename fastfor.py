import time
from collections import deque

start = time.time()
i = 0
deque((i := x for x in range(0,1000000001)),maxlen=0)
elapsed = (time.time() - start) * 1000
print(i)
print(f"elapsed: {elapsed:.4f} ms")