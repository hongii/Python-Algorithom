# 다시 풀어볼 문제 -> 아이디어 구상 못함
T = int(input())
k = int(input())
coins = [list(map(int, input().split())) for _ in range(k)]
cnt = 0


def dfs(x, res):
  global cnt
  if res > T:
    return
  if x == k:
    if res == T:
      cnt += 1
  else:
    for i in range(0, coins[x][1]+1):
      dfs(x+1, res+(coins[x][0]*i))


dfs(0, 0)
print(cnt)
