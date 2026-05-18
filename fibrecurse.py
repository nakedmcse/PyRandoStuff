# Recursive Fibonacci with no memoization
import time

def fib(terms: list[int], target: int) -> list[int]:
    term_len = len(terms)
    if term_len == target + 1:
        return terms
    terms.append(terms[term_len - 1] + terms[term_len - 2])
    return fib(terms, target)

start = time.time()
print(fib([0,1],87).pop())
elapsed = (time.time() - start) * 1000
print(f"elapsed: {elapsed:.4f} ms")