# Chudnovsky with binary splitting
import time, math, sys
from collections import deque

def big_sqrt(v:int) -> int:
    if v < 2:
        return v
    bitlength = len(bin(v)[2:])
    x0 = 1 << ((bitlength + 1) >> 1)
    while True:
        x1 = (x0 + v // x0) >> 1
        if x0 == x1 or x0 == x1 - 1:
            return x0 if x0 <= x1 else x1
        x0 = x1

def chubPiBS(digits: int) -> int:
    c = 640320
    c_cube_div24 = (c**3)//24

    def bs(a0: int, b0: int) -> tuple[int, int, int]:
        results: dict[tuple[int, int], tuple[int, int, int]] = {}
        q = deque()
        q.append((a0, b0))

        while q:
            a, b = q.popleft()
            key = (a, b)

            if key in results:
                continue

            if b - a == 1:
                if a == 0:
                    pab = 1
                    qab = 1
                else:
                    pab = (6 * a - 5) * (2 * a - 1) * (6 * a - 1)
                    qab = a * a * a * c_cube_div24
                tterm = 13591409 + 545140134 * a
                tab = -pab * tterm if (a & 1) == 1 else pab * tterm

                results[key] = (pab, qab, tab)
                continue

            m = (a + b) // 2
            left = (a, m)
            right = (m, b)

            if left in results and right in results:
                pam, qam, tam = results[left]
                pmb, qmb, tmb = results[right]

                pab = pam * pmb
                qab = qam * qmb
                tab = qmb * tam + pam * tmb

                results[key] = (pab, qab, tab)
            else:
                q.append(key)
                if left not in results:
                    q.append(left)
                if right not in results:
                    q.append(right)

        return results[(a0, b0)]

    digits_per_term = int(math.log10(c_cube_div24/6/2/6))
    n = digits//digits_per_term + 1
    p, q, t = bs(0,n)
    sqr_c = big_sqrt(10005*(10**(digits * 2)))
    return (q * 426880 * sqr_c)//t

sys.set_int_max_str_digits(100_000)
start_time = time.time()
print(chubPiBS(100_000))
elapsed = time.time() - start_time
print("100,000 digits:", elapsed)