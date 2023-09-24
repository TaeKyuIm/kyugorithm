directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, -1), (1, 1), (-1, -1), (-1, 1)]
def dfs(x, y):
    """
    x : 세로 인덱스
    y : 가로 인덱스
    height : 높이
    """
    if 0 <= x < n and 0 <= y < m: # 그래프 안의 범위에 드는 경우
        visited[x][y] = True # 방문 처리
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] > graph[x][y]: # 주변이 더 높은 경우
                    return False
                if visited[nx][ny] == False and graph[nx][ny] == graph[x][y]: # 주변을 아직 방문 안했고, 높이가 같은 경우
                    dfs(nx, ny)
        return True

n, m = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(n)]

visited = [[False] * m for _ in range(n)]

cnt = 0

for i in range(n):
    for j in range(m):
        if graph[i][j] > 0 and visited[i][j] == False: # 0보다 크고 아직 방문 안함
            if dfs(i, j): # 참일때(봉우리)
                # print(i, j)
                cnt += 1
print(cnt)