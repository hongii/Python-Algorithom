import sys
filePath_laptop = "C:\\Users\khj77\\OneDrive\\바탕 화면\\Python\\python_Algo_practice\\Python-Algorithom\\7. 동적 계획법\\input.txt"
filePath_desktop = "C:\\Users\\cywoo\\OneDrive\\바탕 화면\\Python\\python_algo_practice\\Python-Algorithom\\7. 동적 계획법\\input.txt"
sys.stdin = open(filePath_desktop, "rt")
n = int(input())
height = [list(map(int, input().split()))  for _ in range(n)]
dp = [[0]*n for _ in range(n)]
dp[0][0] = height[0][0]

def dfs(x, y):
  if x == 0 and y == 0:
    return height[0][0]
  if dp[x][y] != 0:
    return dp[x][y]
  else:
    if x == 0:
      dp[x][y] = dfs(x, y-1) + height[x][y]
    elif y == 0:
      dp[x][y] = dfs(x-1, y) + height[x][y]
    else:
      dp[x][y] = min(dfs(x-1, y) , dfs(x, y-1)) + height[x][y]
    return dp[x][y]

print(dfs(n-1, n-1))
# print(dp)
