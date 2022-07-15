def bsearch_l(x, start, d):
    left = start - 1
    r = len(x)
    while r - left > 1:
        m = (left + r) // 2
        if x[m] < d:
            left = m
        else:
            r = m
    return r


# n = # of places
# m = # of students

def check(d, m, xs):
    # print(f"d = {d}")
    # print(f"xs = {xs}")
    i = 0
    m -= 1
    threshold = xs[i] + d

    for i in range(1, len(xs)):
        if xs[i] >= threshold:
            m -= 1
            if m == 0:
                return True
            threshold = xs[i] + d

    return False


if __name__ == '__main__':
    n, m = list(map(int, input().split()))
    coord = list(map(int, input().split()))
    coord.sort()

    res = -1

    left = 0
    r = coord[-1]

    if left == r:
        if check(1, m, coord):
            res = 1
    else:
        while left < r:
            # print(f"left = {left}, r = {r}")
            mid = (left + r) // 2
            if check(mid, m, coord):
                left = mid + 1
                res = max(res, mid)
            else:
                r = mid

    print(res)

