n, m = map(int, input().split())

inf = int(1e6)

graph = [[inf] * (n+1) for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, n+1):
        if i == j:
            graph[i][j] = 0 # 자기 자신은 0으로 초기화

for _ in range(m):
    i, j = map(int, input().split())
    graph[i][j] = 1 # 비용이 1로 일정
    graph[j][i] = 1 # 친구니 반대 방향도 비용 1로 설정

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
        
result = []

for i in range(1, n+1):
    result.append(sum(graph[i]))

print(result.index(min(result))+1)