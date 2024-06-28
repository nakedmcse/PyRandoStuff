# Collatz
import time
import threading


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


def chunk(start: int, end: int):
    global memos
    esteps = 0
    for i in range(start, end):
        esteps = collatz(i)
        memos[i] = esteps
        if i % 5000000 == 0:
            print(f'Seed:{i} Steps:{esteps}')

memos = [0] * 10_000_000
start_time = time.time()
t1 = threading.Thread(target=chunk, args=(1, 2_500_000))
t1.start()
t2 = threading.Thread(target=chunk, args=(2_500_000, 5_000_000))
t2.start()
t3 = threading.Thread(target=chunk, args=(5_000_000, 7_500_000))
t3.start()
t4 = threading.Thread(target=chunk, args=(7_500_000, 10_000_000))
t4.start()
t1.join()
t2.join()
t3.join()
t4.join()
elapsed = time.time() - start_time
print(f"Collatz time: {elapsed}")