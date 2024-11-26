# 2023 Day24 Part 2
import math
import re


class vector:
    def __init__(self, x: int, y: int, z: int):
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):
        return f'{self.x}, {self.y}, {self.z}'


class hail:
    def __init__(self, position: vector, velocity: vector):
        self.position = position
        self.velocity = velocity

    def __repr__(self):
        return f'{self.position.x}, {self.position.y}, {self.position.z} @ {self.velocity.x}, {self.velocity.y}, {self.velocity.z} ({self.speed()})'

    def speed(self) -> float:
        return math.sqrt(self.velocity.x**2 + self.velocity.y**2 + self.velocity.z**2)


def subtract_vectors(a: vector, b: vector) -> vector:
    return vector(a.x - b.x, a.y - b.y, a.z - b.z)


def dot_product(a: vector, b: vector) -> int:
    return (a.x * b.x) + (a.y * b.y) + (a.z * b.z)


def cross_product(a: vector, b: vector) -> vector:
    return vector((a.y*b.z) - (a.z*b.y), (a.z*b.x) - (a.x*b.z), (a.x*b.y) - (a.y*b.x))


def find_plane(p1: vector, v1: vector, p2: vector, v2: vector):
    p12 = subtract_vectors(p1, p2)
    v12 = subtract_vectors(v1, v2)
    vv = cross_product(v1, v2)
    return (cross_product(p12, v12), dot_product(p12, vv))


def extend_lines(r: int, a: vector, s: int, b: vector, t: int, c: vector) -> vector:
    x = r*a.x + s*b.x + t*c.x
    y = r*a.y + s*b.y + t*c.y
    z = r*a.z + s*b.z + t*c.z
    return vector(x, y, z)


def independent(a: vector, b: vector) -> bool:
    l = cross_product(a, b)
    return l.x != 0 or l.y !=0 or l.z != 0


def on_same_line(a: vector, b: vector, c: vector) -> bool:
    vector_ab = subtract_vectors(b, a)
    vector_ac = subtract_vectors(c, a)
    cross = cross_product(vector_ab, vector_ac)
    return cross.x == 0 and cross.y == 0 and cross.z == 0


def find_rock(p1: hail, p2: hail, p3: hail):
    a, A = find_plane(p1.position, p1.velocity, p2.position, p2.velocity)
    b, B = find_plane(p1.position, p1.velocity, p3.position, p3.velocity)
    c, C = find_plane(p2.position, p2.velocity, p3.position, p3.velocity)

    w = extend_lines(A, cross_product(b, c), B, cross_product(c, a), C, cross_product(a, b))
    t = dot_product(a, cross_product(b, c))
    wt = vector(w.x // t, w.y // t, w.z // t)
    w1 = subtract_vectors(p1.velocity, wt)
    w2 = subtract_vectors(p2.velocity, wt)
    ww = cross_product(w1, w2)

    D = dot_product(ww, cross_product(p2.position, w2))
    E = dot_product(ww, cross_product(p1.position, w1))
    F = dot_product(p1.position, ww)
    scaling = dot_product(ww, ww)

    rock_position = extend_lines(D, w1, -E, w2, F, ww)
    return (rock_position, scaling)


with open('2023_day24_input.txt') as file:
    hail_list = [hail(vector(int(y[0]), int(y[1]), int(y[2])), vector(int(y[3]), int(y[4]), int(y[5])))
                 for y in (re.findall(r'-?\d+', x) for x in file.read().splitlines())]

p1 = hail_list[0]

for i in range(1, len(hail_list)):
    if independent(p1.velocity, hail_list[i].velocity):
        p2 = hail_list[i]
        break

for j in range(i+1, len(hail_list)):
    if independent(p1.velocity, hail_list[j].velocity) and independent(p2.velocity, hail_list[j].velocity):
        p3 = hail_list[j]
        break

rock_pos, scale = find_rock(p1, p2, p3)
print(rock_pos.x // scale, rock_pos.y // scale, rock_pos.z // scale)
answer = (rock_pos.x + rock_pos.y + rock_pos.z) // scale
print(f'Part 2 answer is {answer}')
