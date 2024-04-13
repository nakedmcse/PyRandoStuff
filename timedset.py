import threading
import time

# Extended timer class supporting time remaining and restarting
class ExtTimer(threading.Timer):
  def __init__(self, interval, function, *args, **kwargs):
    super().__init__(interval, self.run_function, *args, **kwargs)
    self.base_function = function
    self.stop_flag = threading.Event()
    self.started_time = None
    self.lock = threading.Lock()

  def run_function(self, *args, **kwargs):
    if not self.stop_flag.is_set():
      self.base_function(*args, **kwargs)

  def start(self):
    with self.lock:
      self.started_time = time.time()
      self.stop_flag.clear()
      super().start()

  def elapsed(self):
      return time.time() - self.started_time

  def remains(self):
    with self.lock:
      return max(0,self.interval - self.elapsed())
    
  def restart(self):
    with self.lock:
      self.stop_flag.set()
      self.started_time = time.time()
      self.timer = ExtTimer(self.interval, self.base_function, *self.args, **self.kwargs)
      self.timer.start()

# Timed set supporting expiring elements with a time to live
class TimedSet(set):
  def __init__(self, initvalue=()):
    self._map = {}
    for x in initvalue: self.add(x)

  def add(self, item, ttl=5):
    timer = ExtTimer(ttl, lambda i=item: self.discard(i))
    timer.start()
    self._map[item] = timer
  
  def discard(self, item):
    self._map.pop(item, None)

  def refresh(self, item):
    if item in self._map:
      self._map[item].restart()

  def getTimeRemaining(self, item):
    return self._map[item].remains() if item in self._map else None

  def __iter__(self):
    return iter(set(self._map.keys()))
  
  def __len__(self):
    return len(set(self._map.keys()))
  
  def __contains__(self, item):
    
    return item in set(self._map)

# Simple tests
members = ["a","b","c","d","e"]    
testSet = TimedSet(members)
testSet.add("X",20);
print(f"Size of timed set: {len(testSet)}")
print("Sleeping 6 secs...")
time.sleep(6);
print(f"Size of timed set: {len(testSet)}")
print(f"Time remaining on X: {testSet.getTimeRemaining('X')}")
print("Refreshing X")
testSet.refresh('X')
print(f"Time remaining on X: {testSet.getTimeRemaining('X')}")
print("DONE")