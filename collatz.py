# Collatz
import numpy as np
import time


def vectorized_collatz(start, end):
    seeds = np.arange(start, end)
    steps = np.zeros_like(seeds)

    while np.any(seeds > 1):
        even_mask = seeds % 2 == 0
        odd_mask = ~even_mask & (seeds > 1)

        seeds[even_mask] //= 2
        seeds[odd_mask] = seeds[odd_mask] * 3 + 1
        steps += even_mask | odd_mask

    return steps


start_time = time.time()
steps = vectorized_collatz(1, 1_000_000)
elapsed = time.time() - start_time

for i in range(0, 1_000_000, 100_000):
    print(f'Seed:{i} Steps:{steps[i-1]}')
print(f"Collatz time: {elapsed}")