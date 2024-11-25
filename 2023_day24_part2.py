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

    def increment_position(self):
        self.position.x += self.velocity.x
        self.position.y += self.velocity.y
        self.position.z += self.velocity.z

    def set_time_index(self, ti: int):
        self.position.x += (self.velocity.x * ti)
        self.position.y += (self.velocity.y * ti)
        self.position.z += (self.velocity.z * ti)


def subtract_vectors(a: vector, b: vector) -> vector:
    return vector(a.x - b.x, a.y - b.y, a.z - b.z)


def cross_product(a: vector, b: vector) -> vector:
    return vector((a.y*b.z) - (a.z*b.y), (a.z*b.x) - (a.x*b.z), (a.x*b.y) - (a.y*b.x))


def on_same_line(a: vector, b: vector, c: vector) -> bool:
    vector_ab = subtract_vectors(b, a)
    vector_ac = subtract_vectors(c, a)
    cross = cross_product(vector_ab, vector_ac)
    return cross.x == 0 and cross.y == 0 and cross.z == 0


def search_vector_history(h1: list[vector], h2: list[vector], h3: list[vector]) -> list[int] | None:
    for f in range(len(h1)):
        for m in range(len(h2)):
            for l in range(len(h3)):
                if on_same_line(h1[f], h2[m], h3[l]):
                    return [f, m, l]
    return None


def get_stone_velocity(hails: list[hail]) -> vector:
    retval = vector(999999, 999999, 999999)

    x_velocities = [h.velocity.x for h in hails]
    x_duplicates = [x for x in x_velocities if x_velocities.count(x) > 1]
    x_dup_hails = [h for h in hails if h.velocity.x == x_duplicates[0]]

    y_velocities = [h.velocity.y for h in hails]
    y_duplicates = [x for x in y_velocities if y_velocities.count(x) > 1]
    y_dup_hails = [h for h in hails if h.velocity.y == y_duplicates[0]]

    z_velocities = [h.velocity.z for h in hails]
    z_duplicates = [x for x in z_velocities if z_velocities.count(x) > 1]
    z_dup_hails = [h for h in hails if h.velocity.z == z_duplicates[0]]

    x_dist = x_dup_hails[0].position.x - x_dup_hails[1].position.x
    y_dist = y_dup_hails[0].position.y - y_dup_hails[1].position.y
    z_dist = x_dup_hails[0].position.z - z_dup_hails[1].position.z

    for i in range(-1000, 1000):
        if i != x_duplicates[0] and x_dist % (i - x_duplicates[0]) == 0 and i < retval.x:
            retval.x = i
        if i != y_duplicates[0] and y_dist % (i - y_duplicates[0]) == 0 and i < retval.y:
            retval.y = i
        if i != z_duplicates[0] and z_dist % (i - z_duplicates[0]) == 0 and i < retval.z:
            retval.z = i

    return retval


with open('2023_day24_test.txt') as file:
    hail_list = [hail(vector(int(y[0]), int(y[1]), int(y[2])), vector(int(y[3]), int(y[4]), int(y[5])))
                 for y in (re.findall(r'-?\d+', x) for x in file.read().splitlines())]

hail_list.sort(key=lambda x: x.speed())

first_hail = hail_list[0]
mid_hail = hail_list[1]
last_hail = hail_list[2]

first_hail_history = []
mid_hail_history = []
last_hail_history = []

i = 0
while i < 500:
    first_hail_history.append(vector(first_hail.position.x, first_hail.position.y, first_hail.position.z))
    mid_hail_history.append(vector(mid_hail.position.x, mid_hail.position.y, mid_hail.position.z))
    last_hail_history.append(vector(last_hail.position.x, last_hail.position.y, last_hail.position.z))
    first_hail.increment_position()
    mid_hail.increment_position()
    last_hail.increment_position()
    i += 1

print(get_stone_velocity(hail_list))

result = search_vector_history(first_hail_history, mid_hail_history, last_hail_history)
if result:
    print(f'Line found at time indexes {result[0]}, {result[1]}, {result[2]}')
    time_diff = result[1] - result[0]
    stone_velocity = vector((mid_hail_history[result[1]].x - first_hail_history[result[0]].x)//time_diff,
                            (mid_hail_history[result[1]].y - first_hail_history[result[0]].y)//time_diff,
                            (mid_hail_history[result[1]].z - first_hail_history[result[0]].z)//time_diff)
    stone_position = vector(first_hail_history[result[0]].x - (result[0] * stone_velocity.x),
                            first_hail_history[result[0]].y - (result[0] * stone_velocity.y),
                            first_hail_history[result[0]].z - (result[0] * stone_velocity.z))
    print(f'Position: {stone_position} Velocity: {stone_velocity}')
else:
    print('No solution found')
