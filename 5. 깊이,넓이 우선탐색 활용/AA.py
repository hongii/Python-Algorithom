n = int(input())
coins = [int(input()) for _ in range(n)]
moneySum = [0] * 3
minGap = sum(coins)


def dfs(x):
  global minGap
  if x == n:
    if max(moneySum) - min(moneySum) < minGap:
      if len(list(set(moneySum))) == 3:  # moneySum에 들어있는 값들이 모두 다른 경우만 허용
        minGap = max(moneySum) - min(moneySum)
  else:
    for i in range(3):
      moneySum[i] += coins[x]
      dfs(x+1)
      moneySum[i] -= coins[x]


dfs(0)
print(minGap)
