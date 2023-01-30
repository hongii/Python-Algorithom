import sys
# filePath = "C:\\Users\khj77\\OneDrive\\바탕 화면\\Python\\python_Algo_practice\\Python-Algorithom\\5. 깊이,넓이 우선탐색 활용\\input.txt"
# sys.stdin = open(filePath, "rt")

n, m = map(int, input().split())
maxScoreSum = 0
score = []
for i in range(n):
  score.append(list(map(int, input().split())))


def dfs(x, scoreSum, time):
  global maxScoreSum
  if time > m:
    return

  else:
    if maxScoreSum < scoreSum:
        maxScoreSum = scoreSum
    for i in range(x, n):
      # print(x, scoreSum, time, maxScoreSum)
      dfs(i+1, scoreSum+score[i][0], time+score[i][1])


dfs(0, 0, 0)
print(maxScoreSum)
