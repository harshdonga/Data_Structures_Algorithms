import sys
from itertools import chain

# def fast_count_segments(starts, ends, points):
#     out = []
#     ans = []
#     cnt = 0
#     for i in range(len(starts)):
#         out += list(range(starts[i],ends[i]+1))
#     out = set(out)
#     for i in points:
#         if i not in out:
#             ans.append(0)
#         else:
#             for j in range(len(starts)):
#                 if starts[j] < i and ends[j] > i:
#                     cnt += 1
#             ans.append(cnt)
#     return ans

def fast_count_segments(starts, ends, points):
    cnt = [0] * len(points)
    start_points = zip(starts, ['l'] * len(starts), range(len(starts)))
    end_points = zip(ends, ['r'] * len(ends), range(len(ends)))
    point_points = zip(points, ['p'] * len(points), range(len(points)))

    sort_list = chain(start_points, end_points, point_points)
    sort_list = sorted(sort_list, key=lambda a: (a[0], a[1]))
    segment = 0
    i = 0
    for num, letter, index in sort_list:
        if letter == 'l':
            segment += 1
        elif letter == 'r':
            segment -= 1
        else:
            cnt[index] = segment
            i += 1
    return cnt

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[1]
    starts = data[2:2 * n + 2:2]
    ends   = data[3:2 * n + 2:2]
    points = data[2 * n + 2:]
    cnt = fast_count_segments(starts, ends, points)
    for x in cnt:
        print(x, end=' ')