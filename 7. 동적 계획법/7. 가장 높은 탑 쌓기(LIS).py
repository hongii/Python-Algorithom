import sys
filePath_laptop = "C:\\Users\khj77\\OneDrive\\바탕 화면\\Python\\python_Algo_practice\\Python-Algorithom\\7. 동적 계획법\\input.txt"
filePath_desktop = "C:\\Users\\cywoo\\OneDrive\\바탕 화면\\Python\\python_algo_practice\\Python-Algorithom\\7. 동적 계획법\\input.txt"
sys.stdin = open(filePath_desktop, "rt")
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


