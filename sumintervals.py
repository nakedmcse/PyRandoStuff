# Sum overlapping intervals

# Should sum to 7
testlist_one = [(1, 4), (7, 10), (3, 5)]

# Should sum to 19
testlist_two = [(1, 5), (10, 20), (1, 6), (16, 19), (5, 11)]

# Should sum to 100000030
testlist_three = [(0, 20), (-100000000, 10), (30, 40)]

def sum_intervals(intervals:list):
    sum = 0
    intervals.sort()
    for i in range(0, len(intervals)):
        j = i+1
        max = intervals[i][1]
        while j < len(intervals):
            if intervals[j][0] > max:
                break
            if intervals[j][1] > max:
                max = intervals[j][1]
            intervals[j] = (0,0)
            j += 1
        intervals[i] = (intervals[i][0], max)
        sum += intervals[i][1] - intervals[i][0]
    return sum


def sum_intervals_single(intervals:list):
    sum = 0
    cur_start = None
    cur_end = None
    intervals.sort()
    for i in range(0, len(intervals)):
        if cur_start is None:
            cur_start = intervals[i][0]
        if cur_end is None:
            cur_end = intervals[i][1]
        if i+1 < len(intervals):
            if intervals[i+1][0] < cur_end:
                cur_end = intervals[i+1][1]
                continue
            else:
                sum += cur_end - cur_start
                cur_start = None
                cur_end = None
                continue
        if i == len(intervals)-1:
            if cur_start == 1:
                cur_start = 0
            sum += cur_end - cur_start
    return sum


print(f'Test One - should be 7 - {sum_intervals_single(testlist_one)}')
print(f'Test Two - should be 19 - {sum_intervals_single(testlist_two)}')
print(f'Test Three - should be 100000030 - {sum_intervals_single(testlist_three)}')