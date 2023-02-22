import sys
filePath_laptop = "C:\\Users\khj77\\OneDrive\\바탕 화면\\Python\\python_Algo_practice\\Python-Algorithom\\7. 동적 계획법\\input.txt"
filePath_desktop = "C:\\Users\\cywoo\\OneDrive\\바탕 화면\\Python\\python_algo_practice\\Python-Algorithom\\7. 동적 계획법\\input.txt"
sys.stdin = open(filePath_desktop, "rt")
n = int(input())
height = [list(map(int, input().split()))  for _ in range(n)]
dp = [[0]*n for _ in range(n)]
dp[0][0] = height[0][0]

# 이동 가능한 방향은 오른쪽 또는 아래쪽이므로 dp테이블에서 맨처음 열(→)과 맨 처음 행(↓)은 height[i][j]의 누적합산 값으로 초기화 시키면 된다.
for i in range(1, n):
  dp[0][i] = dp[0][i-1] + height[0][i]
  dp[i][0] = dp[i-1][0] + height[i][0]

for i in range(1, n):
  for j in range(1, n):
    # 현재 (i,j)좌표 기준으로 왼쪽 또는 윗쪽의 dp값과 비교해서 더 작은 값에다 height[i][j]값을 더한 값이 dp[i][j]가 된다.
    dp[i][j] = min(dp[i][j-1], dp[i-1][j]) + height[i][j]

print(dp[n-1][n-1])