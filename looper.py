# Looper

def make_looper(s: str):
    def looper():
        i = 0
        while True:
            yield s[i]
            i = (i + 1) % len(s)

    l = looper()
    return lambda: next(l)

looper_a = make_looper("abc")
looper_b = make_looper("def")

print(looper_a())
print(looper_a())
print(looper_a())
print(looper_a())
print(looper_b())