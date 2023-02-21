n = int(input())
bricks = [list(map(int, input().split())) for _ in range(n)] #[[밑면넓이, 높이, 무게],[...]...]
bricks.sort(reverse=True)
dp = [0] * n

dp[0] = bricks[0][1]
for i in range(1, n):
  height = bricks[i][1]
  for j in range(i):
    if bricks[j][2] > bricks[i][2]:
      height = max(height, dp[j]+bricks[i][1])
  dp[i] = height
print(max(dp))


