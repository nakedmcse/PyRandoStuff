# Project Euler 191
# https://projecteuler.net/problem=191
import time
from functools import cache

# Reverse brute force in solution space
winning_combos = []
def get_initial_winning_combos():
    global winning_combos
    options = ['o','l','a']
    for a in options:
        for b in options:
            for c in options:
                combo = a+b+c
                if 'aaa' in combo: continue
                if combo.count('l') > 1: continue
                a_con_count = 0
                if c == 'a' and b == 'a': a_con_count = 2
                elif c == 'a' and b != 'a': a_con_count = 1
                winning_combos.append((a_con_count, combo.count('l')))

def extend_winning_combos():
    global winning_combos
    appending = []
    options = ['o','l','a']
    for a in options:
        for c in winning_combos:
            new_a_con_count = 0
            if a == 'a':
                new_a_con_count = c[0] + 1
            if new_a_con_count > 2: continue
            new_l_count = c[1] + (1 if a == 'l' else 0)
            if new_l_count > 1: continue
            appending.append((new_a_con_count, new_l_count))
    winning_combos = appending

def reverse_brute_force() -> int:
    get_initial_winning_combos()
    for _ in range(26): extend_winning_combos()
    return len(winning_combos)

# Cached recursive solution
@cache
def get_winning_combos(day: int, a_con_count: int, l_count: int) -> int:
    retval = 0

    if a_con_count == 3: return 0   # 3 consecutive absence end condition
    if l_count > 1: return 0        # more than 1 late end condition
    if day == 30: return 1          # 30 days made winning end condition

    retval += get_winning_combos(day+1, 0, l_count)             # add 'o', reset a, l stays same
    retval += get_winning_combos(day+1, 0, l_count+1)           # add 'l', reset a, increment l
    retval += get_winning_combos(day+1, a_con_count+1, l_count) # add 'a', increment a consec, l stays same

    return retval

start_time = time.time()
solution_recursive = get_winning_combos(0,0,0)
print(f'Cached recursive: {solution_recursive} in {time.time() - start_time} seconds')

start_time = time.time()
solution_rbf = reverse_brute_force()
print(f'Solution space brute force: {solution_rbf} in {time.time()-start_time} seconds')