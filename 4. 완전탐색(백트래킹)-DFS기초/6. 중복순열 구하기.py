# 다시 풀어볼 문제 -> 여러가닥이 있는 트리
import sys
filePath = "C:\\Users\khj77\\OneDrive\\바탕 화면\\Python\\python_Algo_practice\\Python-Algorithom\\4. 완전탐색(백트래킹)-DFS기초\\input.txt"
sys.stdin = open(filePath, "rt")
n, m = map(int, input().split())
res = [0] * m
cnt = 0


def dfs(x): # x는 depth
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