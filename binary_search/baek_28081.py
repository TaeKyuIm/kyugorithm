import bisect

W, H, K = map(int, input().split())
N = int(input())

# 가로 방향 자르는 위치 -> y의 위치
y_location = list(map(int, input().split()))
y_location.insert(0, 0) # 제일 앞에 0 추가
y_location.append(H)

M = int(input())

x_location = list(map(int, input().split()))
x_location.insert(0, 0) # 제일 앞에 0 추가
x_location.append(W)

delta_y = [y_location[i+1] - y_location[i] for i in range(N+1)]
# N-1개
delta_x = [x_location[i+1] - x_location[i] for i in range(M+1)]
# M-1개

delta_y.sort()
delta_x.sort()

count = 0

for dy in delta_y:
    # K/dy 값이 dx 배열에서 몇 개 있는지 찾기
    limit = K / dy
    index = bisect.bisect_right(delta_x, limit)  # limit 값보다 작은 dx의 개수 찾기
    count += index

print(count)