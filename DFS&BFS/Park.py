from collections import deque
INF = 10**9


def bfs(G, visited, s, d, p):
    vertex_queue = deque([s])
    while vertex_queue:
        v = vertex_queue.popleft()
        visited[v] = 2
        for u in G[v]:
            if not visited[u]:
                visited[u] = 1
                vertex_queue.append(u)
                d[u] = d[v] + 1
                p[u] = v


if __name__ == '__main__':
    N, M = map(int, input().split())

    matrix = [[-1 for i in range(M)] for j in range(N)]
    current = None
    cnt = 0
    for i in range(N):
        data = input()
        for j in range(M):
            if data[j] != '#':
                matrix[i][j] = cnt
                cnt += 1
                if data[j] == 'E':
                    current = matrix[i][j]
                elif data[j] == 'X':
                    end = matrix[i][j]
    G = [[] for i in range(cnt)]

    for x in range(N):
        for y in range(M):
            if matrix[x][y] != -1 and y <= M - 2 and matrix[x][y + 1] != -1:
                G[matrix[x][y]].append(matrix[x][y + 1])
            if matrix[x][y] != -1 and y > 0 and matrix[x][y - 1] != -1:
                G[matrix[x][y]].append(matrix[x][y - 1])
            if matrix[x][y] != -1 and x <= N - 2 and matrix[x + 1][y] != -1:
                G[matrix[x][y]].append(matrix[x + 1][y])
            if matrix[x][y] != -1 and x > 0 and matrix[x - 1][y] != -1:
                G[matrix[x][y]].append(matrix[x - 1][y])

    d = [-1] * len(G)
    p = [0] * len(G)
    d[current] = 0
    visited = [0] * len(G)

    bfs(G, visited, current, d, p)

    print(d[end])

