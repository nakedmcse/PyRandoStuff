import random
import time
import os
from multiprocessing import Pool

BT = None

def init_worker(bt):
    global BT
    BT = bt

def multiply_rows(rows_a):
    return [
        [sum(x * y for x, y in zip(row_a, col_b)) for col_b in BT]
        for row_a in rows_a
    ]

def chunks(seq, size):
    for i in range(0, len(seq), size):
        yield seq[i:i + size]

if __name__ == "__main__":
    n = 1000
    a = [[random.random() for _ in range(n)] for _ in range(n)]
    b = [[random.random() for _ in range(n)] for _ in range(n)]

    bt = list(zip(*b))

    workers = os.cpu_count() or 4
    chunk_size = max(1, n // workers)

    start = time.time()

    with Pool(workers, initializer=init_worker, initargs=(bt,)) as pool:
        parts = pool.map(multiply_rows, chunks(a, chunk_size))

    c = [row for part in parts for row in part]

    elapsed = (time.time() - start) * 1000
    print(f"elapsed: {elapsed:.4f} ms")