import sys

n = int(input())
coins = list(map(int, input().split()))
coins.sort(reverse=True)
m = int(input())
minCnt = sys.maxsize

# solution


def dfs(x, res):
  global minCnt
  if res > m:
    return
  if x >= minCnt:
    return
  if res == m:
    if x < minCnt:
      minCnt = x
  else:
    for i in range(n):
      dfs(x+1, res+coins[i])


dfs(0, 0)
print(minCnt)

