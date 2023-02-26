n, m = map(int, input().split())
M = int(1e9) # M = 10억(무한대 값)
dp = [[M] * (n+1) for _ in range(n+1)]

for i in range(1, n+1): # 자기 자신으로 가는 비용은 0으로 갱신
  dp[i][i] = 0

# dp테이블 초기값은 인접행렬 간선 가중치 값으로 갱신
for i in range(m):
  i, j, w = map(int, input().split())
  dp[i][j] = w

# 모든 정점에서 모든 정점으로 가는 최소비용 구하기
for k in range(1, n+1):
  for i in range(1, n+1):
    for j in range(1, n+1):
      dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])

for i in range(1, n+1):
  for j in range(1, n+1):
    if dp[i][j] == 1e9:
      print("M", end=" ")
    else:
      print(dp[i][j], end=" ")
  print()
