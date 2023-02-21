n = int(input())
arr = list(map(int, input().split()))
arr.insert(0, 0)

dp = [0] * (n+1)
dp[1] = 1
for i in range(2, n+1):
  length = 1
  for j in range(1, i):
    if arr[j] < arr[i]:
      length = max(length, dp[j]+1)
  dp[i] = length

print(max(dp))