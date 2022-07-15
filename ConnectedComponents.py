def dfs_nonrec_1(G, visited, s, vertexes):
    vertex_stack = [s]
    while vertex_stack:
        v = vertex_stack.pop()
        if not visited[v]:
            vertexes.add(v)

            visited[v] = True
            for u in G[v]:
                if not visited[u]:
                    vertexes.add(u)
                    vertex_stack.append(u)


if __name__ == '__main__':
    N, M = map(int, input().split())
    G = [[] for i in range(N)]

    for i in range(M):
        x, y = map(int, input().split())
        if x != y:
            G[x].append(y)
            G[y].append(x)

    visited = [False] * len(G)
    allV = []
    n_components = 0

    for i in range(len(G)):
        if not visited[i]:
            n_components += 1
            vertexes = set()
            dfs_nonrec_1(G, visited, i, vertexes)
            allV.append(vertexes)

    print(n_components)
    for segment in allV:
        print(len(segment))
        print(" ".join(list(map(str, segment))))

