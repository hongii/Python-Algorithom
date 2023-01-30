import sys
filePath = "C:\\Users\khj77\\OneDrive\\바탕 화면\\Python\\python_Algo_practice\\Python-Algorithom\\5. 깊이,넓이 우선탐색 활용\\input.txt"
sys.stdin = open(filePath, "rt")

n = int(input())
sevenDays = [list(map(int, input().split())) for _ in range(n)]
sevenDays.insert(0, [0, 0])  # 1일 == index 1로 맞추기 위해 맨 앞 0번 index에는 더미값 [0,0]을 넣어줌
maxProfit = 0

def dfs(x, profit):
  global maxProfit
  if x > n+1:
    return
  if x == n+1 or (x == n and sevenDays[x][0] > 1):
    if profit > maxProfit:
      maxProfit = profit
  else:
      dfs(x+sevenDays[x][0], profit+sevenDays[x][1])
      dfs(x+1, profit)

dfs(1, 0)
print(maxProfit)