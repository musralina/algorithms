def isInRange(a, l, r):
    li = bsearch_l(score, l)
    ri = bsearch_r(score, r)
    print(ri - li)


def bsearch_l(x, key):
    l = -1
    r = len(x)
    while r - l > 1:
        m = (l + r) // 2
        if x[m] < key:
            l = m
        else:
            r = m
    return r


def bsearch_r(x, key):
    l = -1
    r = len(x)
    while r - l > 1:
        m = (l + r) // 2
        if x[m] <= key:
            l = m
        else:
            r = m
    return r


if __name__ == '__main__':
    N, M = map(int, input().strip().split())
    score = list(map(int, input().strip().split()))
    score.sort()

    for i in range(M):
        l, r = map(int, input().strip().split())
        isInRange(score, l, r)

