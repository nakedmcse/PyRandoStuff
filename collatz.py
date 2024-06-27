# Collatz
import time
import threading


class ThreadWithResult(threading.Thread):
    def __init__(self, group=None, target=None, name=None, args=(), kwargs={}, *, daemon=None):
        def function():
            self.result = target(*args, **kwargs)
        super().__init__(group=group, target=function, name=name, daemon=daemon)


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
for i in range(1, 10_000_000, 4):
    t1 = ThreadWithResult(target=collatz, args=(i,))
    t1.start()
    t2 = ThreadWithResult(target=collatz, args=(i+1,))
    t2.start()
    t3 = ThreadWithResult(target=collatz, args=(i+2,))
    t3.start()
    t4 = ThreadWithResult(target=collatz, args=(i+3,))
    t4.start()
    t1.join()
    memos[i] = t1.result
    t2.join()
    memos[i+1] = t2.result
    t3.join()
    memos[i+2] = t3.result
    t4.join()
    memos[i+4] = t4.result
    if i % 1000000 == 0:
        print(f'Seed:{i} Steps:{esteps}')
elapsed = time.time() - start_time
print(f"Collatz time: {elapsed}")