# Project Euler 191
# https://projecteuler.net/problem=191

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
                winning_combos.append(combo)

def extend_winning_combos():
    global winning_combos
    appending = []
    options = ['o','l','a']
    for a in options:
        for c in winning_combos:
            newcombo = c+a
            if 'aaa' in newcombo: continue
            if newcombo.count('l') > 1: continue
            appending.append(newcombo)
    winning_combos = appending

get_initial_winning_combos()
day = 4
for _ in range(27):
    print(day)
    extend_winning_combos()
    day += 1
print(len(winning_combos))