import time

# Lambda vs Foreach
num = [1,2,3,4,5]

#foreach version
for_start_time = time.time()

for i in num:
    if i%2==0:
        continue
    print(i**2,end=' ')

for_end_time = time.time()
print()
print(f"Foreach Execution time {(for_end_time - for_start_time) * 1000} ms")
print()

#lambda version
lamb_start_time = time.time()

list(map(lambda odd_square: print(odd_square**2,end=' ') if odd_square % 2 != 0 else None, num))

lamb_end_time = time.time()
print()
print(f"Lambda Execution time {(lamb_end_time - lamb_start_time) * 1000} ms")
print()

#filtered list
filt_start_time = time.time()

print(list(filter(lambda x: x is not None,map(lambda odd_square: None if odd_square%2==0 else odd_square**2,num))))

filt_end_time = time.time()
print(f"Filtered List Execution time {(lamb_end_time - lamb_start_time) * 1000} ms")