import math


def counting_stars(yes: int, no: int) -> int:
    if yes == 0:
        return 1
    return math.ceil((yes / (yes + no))*5)


print(counting_stars(100,0))
print(counting_stars(80,20))
print(counting_stars(0,20))
print(counting_stars(21,79))
print(counting_stars(19,81))
print(counting_stars(0, 0))
