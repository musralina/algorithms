inf = 10 ** 9


def bellman_ford(N, A, s, f, K):
    d = [[inf] * N for i in range(N)]
    for i in range(N):
        d[i][s] = 0

    for i in range(N - 1):
        for (v, u, w) in A:
            if d[i][u] > d[i - 1][v] + w:
                d[i][u] = d[i - 1][v] + w
    return d[K - 1][f]


if __name__ == '__main__':
    N, s, f, K = map(int, input().split())
    A = []
    for i in range(N):
        c = list(map(int, input().split()))
        for j in range(N):
            if c[j] != -1:
                A.append(tuple((i, j, c[j])))
    cost = bellman_ford(N, A, s, f, K)
    if (K == 0) or (cost >= inf):
        print('-1')
    elif s == f:
        print(0)
    else:
        print(cost)

