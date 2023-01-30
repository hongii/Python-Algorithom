n = int(input())
sevenDays = [list(map(int, input().split())) for _ in range(n)]
# 1일 == index 1로 맞추기 위해 맨 앞 0번 index에는 더미값 [0,0]을 넣어줌
sevenDays.insert(0, [0, 0])
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
