def dfs(graph, i, j, visited, army):
    if i < 0 or i >= m or j < 0 or j >= n or graph[i][j] != army or visited[i][j]:
        return 0

    visited[i][j] = True

    size = 1

    for x, y in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        size += dfs(graph, i + x, j + y, visited, army)
    
    return size

n, m = map(int, input().split())
visited = [[False for _ in range(n)] for _ in range(m)]

graph = []
for i in range(m):
    graph.append(list(map(str, input())))

w_result = []
for i in range(m):
    for j in range(n):
        if graph[i][j] == "W" and not visited[i][j]:
            w_result.append(dfs(graph, i, j, visited, "W"))

visited = [[False for _ in range(n)] for _ in range(m)]

b_result = []
for i in range(m):
    for j in range(n):
        if graph[i][j] == "B" and not visited[i][j]:
            b_result.append(dfs(graph, i, j, visited, "B"))

sum_w = sum([w**2 for w in w_result])
sum_b = sum([b**2 for b in b_result])

print(sum_w, sum_b)