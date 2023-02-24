n = int(input())
coins = list(map(int, input().split()))
m = int(input())
coins.sort()
dp = [501] * (m+1)
dp[0] = 0

for coin in coins:
  for j in range(coin, m+1):
    dp[j] = min(dp[j], dp[j-coin] + 1)
print(dp[m])