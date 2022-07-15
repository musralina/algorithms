from heapq import heappush, heappop
inf = 10 ** 9


if __name__ == '__main__':
    N, M = map(int, input().split())
    s, h1 = map(int, input().split())
    G = [{} for i in range(N)]
    for i in range(M):
        x, y, weight = map(int, input().split())
        G[x][y] = weight
        G[y][x] = weight

    h = []
    d = [inf] * N
    v = -1
    # added fictitious vertex to simplify
    # while with heappop:
    S = {-1}
    d[s] = 0
    heappush(h, (d[s], s, None))
    path = {}
    while h:
        while v in S and h:
            tmp = heappop(h)
            v = tmp[1]
        if v not in S:
            S.add(v)
            path[tmp[1]] = (tmp[0], tmp[2])
            if v == h1:
                break
            for u in G[v]:
                new_d = d[v] + G[v][u]
                if new_d < d[u]:
                    heappush(h, (new_d, u, v))
                    d[u] = new_d
    if h1 not in S:
        print('-1')
    else:
        dd_len = 0
        i = h1
        path_ans = [i]
        while i != s:
            dd_len += path[i][0]
            i = path[i][1]
            path_ans.append(i)
        print(path[h1][0])
        print(len(path_ans))
        path_ans.reverse()
        print(' '.join(map(str, path_ans)))

