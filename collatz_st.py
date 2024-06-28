# Collatz
import time


def collatz(seed: int):
    global memos
    steps = 0
    while seed > 1:
        if seed < len(memos) and memos[seed] > 0:
            steps += memos[seed]
            break

        if seed % 2 == 0:
            steps += 1
            seed = seed // 2
            continue

        steps += 1
        seed = seed * 3 + 1

    return steps


esteps = 0
memos = [0] * 10_000_000
start_time = time.time()
for i in range(1, 10_000_000):
    esteps = collatz(i)
    memos[i] = esteps
    if i % 5000000 == 0:
        print(f'Seed:{i} Steps:{esteps}')
elapsed = time.time() - start_time
print(f"Collatz time: {elapsed}")