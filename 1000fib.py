def fib(digits: int) -> int:
    i = 2
    memo = [1,1,2]
    while len(str(memo[2])) < digits:
        memo[0] = memo[1]
        memo[1] = memo[2]
        memo[2] = memo[0] + memo[1]
        i += 1
    return i+1

print(f'First element with 3 digits: {fib(3)}')
print(f'First element with 1000 digits: {fib(1000)}')