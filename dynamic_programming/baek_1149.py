import sys

def get_second_price(x):
    x.remove(min(x))
    return min(x)

read = sys.stdin.readline

n = int(read())

prices = [list(map(int, read().split())) for _ in range(n)]

dp = [[0] * 3 for _ in range(n+1)]

for i in range(1,n+1):
    dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + prices[i-1][0]
    dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + prices[i-1][1]
    dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + prices[i-1][2]

print(min(dp[n][0], dp[n][1], dp[n][2]))