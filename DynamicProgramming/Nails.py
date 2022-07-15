import bisect


def myD(x, l):
    dist = []
    x.sort()
    for i in range(l - 1):
        dist.append(x[i + 1] - x[i])
    return dist


def myLis(s, l):
    N = l - 1
    d = [None] * N
    d[0] = s[0]
    if N < 3:
        thread = sum(s)
    else:
        d[1] = s[1]
        d[2] = s[2]
        for i in range(3, N):
            d[i] = min(d[i - 1], d[i - 2]) + s[i]
        thread = d[N - 1] + d[0]
    return thread


if __name__ == '__main__':
    l = int(input())
    x = list(map(int, input().split()))
    dist = myD(x, l)
    ans = myLis(dist, l)
    print(ans)

