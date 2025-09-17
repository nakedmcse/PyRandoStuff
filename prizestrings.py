# Project Euler 191
# https://projecteuler.net/problem=191
import time

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

start_time = time.time()
solution_rbf = reverse_brute_force()
print(f'Solution space brute force: {solution_rbf} in {time.time()-start_time} seconds')