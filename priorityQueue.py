# Priority Queue example
import heapq, time, random

RANGE = 10000000

simple_prio = []
print("Priority Enqueued 1:1, 2:1, 3:1, 4:5, 5:9")
heapq.heappush(simple_prio, (-1, 1))
heapq.heappush(simple_prio, (-1, 2))
heapq.heappush(simple_prio, (-1, 3))
heapq.heappush(simple_prio, (-5, 4))
heapq.heappush(simple_prio, (-9, 5))

# Dequeue order check
test_out = []
while simple_prio:
    test_out.append(heapq.heappop(simple_prio)[1])
print("Simple Priority Queue Dequeued:", ' '.join(map(str, test_out)))

# Speed test
pairs = [(0-random.randint(1, 10), random.randint(0, RANGE)) for _ in range(RANGE)]
start_time = time.time()
for priority, value in pairs:
    heapq.heappush(simple_prio, (priority, value))
elapsed = time.time() - start_time
print("Simple priority queue enqueue time:", elapsed)

count = 0
start_time = time.time()
while simple_prio:
    heapq.heappop(simple_prio)
    count += 1
elapsed = time.time() - start_time
print("Simple priority queue dequeued items:", count)
print("Simple priority queue dequeue time:", elapsed)
print("-----")