n, m = map(int, input().split())
res = [0] * m
cnt = 0


def dfs(x):  # x는 depth
  global cnt
  if x == m:
    cnt += 1
    for i in range(m):
      print(res[i], end=" ")
    print()
  else:
    for i in range(1, n+1):
      res[x] = i
      dfs(x+1)


dfs(0)
print(cnt)
