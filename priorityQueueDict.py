# Priority Queue implemented with dictionary
from collections import deque
import time, random

# class
class dict_priority_queue:
    def __init__(self):
        self.queue = {}
        self.queue[1] = deque([])

    def empty(self):
        return len(self.queue) == 0
    
    def size(self):
        return len(self.queue)
    
    def enqueue(self, dataitem, prio):
        currentq = self.queue.get(prio)
        if currentq == None:
            currentq = deque([dataitem])
            self.queue[prio] = currentq
        else:
            currentq.append(dataitem)

    def dequeue(self):
        if self.empty(): return None
        maxkey = max(self.queue.keys())
        currentq = self.queue.get(maxkey)
        retval = currentq.popleft()
        if len(currentq)==0:
            del self.queue[maxkey]
        return retval

def get_pair():
    return (0-random.randint(1, 10), random.randint(0, RANGE))

RANGE = 10000000

simple_prio = dict_priority_queue();
print("Priority Enqueued 1:1, 2:1, 3:1, 4:5, 5:9")
simple_prio.enqueue(1, 1)
simple_prio.enqueue(2, 1)
simple_prio.enqueue(3, 1)
simple_prio.enqueue(4, 5)
simple_prio.enqueue(5, 9)

# Dequeue order check
test_out = []
while not simple_prio.empty():
    test_out.append(simple_prio.dequeue())
print("Simple Priority Queue Dequeued:", ' '.join(map(str, test_out)))

# Speed test
pairs = [get_pair() for _ in range(RANGE)]
start_time = time.time()
for pair in pairs:
    simple_prio.enqueue(pair[1],pair[0])
elapsed = time.time() - start_time
print("Simple priority queue enqueue time:", elapsed)

count = 0
start_time = time.time()
while not simple_prio.empty():
    simple_prio.dequeue()
    count += 1
elapsed = time.time() - start_time
print("Simple priority queue dequeued items:", count)
print("Simple priority queue dequeue time:", elapsed)
print("-----")