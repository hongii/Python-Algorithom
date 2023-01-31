k = int(input())
weight = list(map(int, input().split()))
s = sum(weight)
check = [0] * (s+1)
cnt = 0


def dfs(x, res):
  if x == k:
    if res > 0:
      check[res] = 1
  else:
    dfs(x+1, res+weight[x])
    dfs(x+1, res-weight[x])
    dfs(x+1, res)


dfs(0, 0)
for i in range(1, s+1):
  if check[i] == 0:  # 측정 불가능한 물의 무게
    cnt += 1
print(cnt)
