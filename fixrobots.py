# Find the minimum distance to factories for robots.
#  Robots are list of x coords for initial position
#  Factories are x coord and capacity
#  Solve for minimum distance to get all robots to a factory, respecting capacity limit


def min_total_dist(robots: list[int], factories: list[list[int]]) -> int:
    retval = float('inf')
    robots.sort()
    factories.sort()

    # evaluate each robot as the start
    for rb_idx in range(len(robots)):
        possible_val = 0
        if rb_idx > 0:
            robots = [robots[(i+rb_idx) % len(robots)] for i, x in enumerate(robots)]

        # convert factories to multiple slot entries, to account for capacity
        slots = []
        for position, capacity in factories:
            slots.extend([position] * capacity)
        slots.sort()

        for robot_pos in robots:
            min_distance = float('inf')
            closest_slot_index = None

            # check each slot to find the closest available one
            for i, slot_pos in enumerate(slots):
                distance = abs(robot_pos - slot_pos)
                if distance < min_distance:
                    min_distance = distance
                    closest_slot_index = i

            # assign the closest slot, remove it from slots
            possible_val += min_distance
            slots.pop(closest_slot_index)

        if possible_val < retval:
            retval = possible_val

    return retval


print("Example 1: Should be 4, ", min_total_dist([0, 4, 6], [[2, 2], [6, 2]]))
print("Example 2: Should be 2, ", min_total_dist([1, -1], [[-2, 1], [2, 1]]))
print("Example 3: Should be 6, ", min_total_dist([9, 11, 99, 101], [[10, 1], [7, 1], [14, 1], [100, 1], [96, 1], [103, 1]]))
print("Example 4: Should be 509199280, ", min_total_dist([670355988,403625544,886437985,224430896,126139936,-477101480,-868159607,-293937930], [[333473422,7],[912209329,7],[468372740,7],[-765827269,4],[155827122,4],[635462096,2],[-300275936,2],[-115627659,0]]))
print("Example 5: Should be 1546649980, ", min_total_dist([-130743012,30616327,665137438,-607129880,333278053,824237381,209140304,-21439914,-728431071,-26955918,-570435494,-320226115,-922013064,-228553160,468665987,879432909,-514864202,-668531403,-678242745,-418104261,199254410,-792384378,741930631],
                                                 [[-456262106,1],[58412189,11],[967520832,9],[564041132,8],[-443010337,8],[990138357,22],[-10111256,12],[-140527933,14],[533615261,8],[-963214494,4],[893755326,23],[-865481531,8],[762205277,14],[288241408,11],[-133736866,0],[177042365,11],[138164674,17],[437863739,21],[889552593,8],[-161328206,8],[-968994624,9],[607416877,15]]))
