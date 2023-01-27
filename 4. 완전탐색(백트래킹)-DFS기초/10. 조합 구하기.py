import sys
filePath = "C:\\Users\khj77\\OneDrive\\바탕 화면\\Python\\python_Algo_practice\\Python-Algorithom\\4. 완전탐색(백트래킹)-DFS기초\\input.txt"
sys.stdin = open(filePath, "rt")

n, m = map(int, input().split())
res = [0] * m
cnt = 0

def dfs(x, startNum):
  global cnt
  if x < m and startNum > n:
    return
  if x == m or startNum > n:
    cnt += 1
    print(*res)
  else:
    for i in range(startNum, n+1):
      res[x] = i
      dfs(x+1, i+1)
      

dfs(0, 1)
print(cnt)