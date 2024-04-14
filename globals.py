# Fun with globals
counter = 0

def increment_counter():
    globals()["counter"] += 1

print(counter)
increment_counter()
print(counter)
increment_counter()
print(counter)
increment_counter()