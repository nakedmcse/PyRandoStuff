def powerdigitsum(level: int) -> int:
    return sum(int(c) for c in str(2 ** level))

print(f'2 to 15: {powerdigitsum(15)} ({2 ** 15})')
print(f'2 to 1000: {powerdigitsum(1000)} ({2 ** 1000})')
print(f'2 to 10000: {powerdigitsum(10000)} ({2 ** 10000})')