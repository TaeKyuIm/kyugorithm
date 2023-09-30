from collections import deque
n, m = map(int, input().split())
# n : x좌표, m : y좌표
inf = int(1e6)
visited = [[False]*n for _ in range(m)]
result = [[inf]*n for _ in range(m)]

graph = []

for _ in range(m):
    temp = str(input())
    graph.append([int(t) for t in temp])
    
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    visited[y][x] = True
    result[y][x] = 0
    
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            
            if not visited[ny][nx]:
                visited[ny][nx] = True
                if graph[ny][nx] == 0:
                    result[ny][nx] = result[y][x]
                    queue.appendleft((nx, ny))
                else:
                    result[ny][nx] = result[y][x] + 1
                    queue.append((nx, ny))

bfs(0, 0)                
print(result[m-1][n-1])