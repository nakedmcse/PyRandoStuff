# Project Euler Problem 548
# https://projecteuler.net/problem=548
from functools import cache

@cache
def gozinta(c: int, target: int) -> int:
    if c == target: return 1
    total = 0
    for i in range(c+1, target + 1):
        if i % c == 0: total += gozinta(i, target)
    return total

print(gozinta(1,12))
print(gozinta(1,48))
print(gozinta(1,120))

for j in range(2,1000):
    g = gozinta(1,j)
    print(f'{j} - {g}')
