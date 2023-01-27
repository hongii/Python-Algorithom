# 상태트리 (가지가 여러개인 트리)
import sys
filePath = "C:\\Users\khj77\\OneDrive\\바탕 화면\\Python\\python_Algo_practice\\Python-Algorithom\\4. 완전탐색(백트래킹)-DFS기초\\input.txt"
sys.stdin = open(filePath, "rt")

n, k = map(int, input().split())
numList = list(map(int, input().split()))
m = int(input())
cnt = 0


def dfs(x, startNum, sum):
  global cnt
  if x == k:
    if sum % m == 0:
      cnt += 1
  else:
    for i in range(startNum, n):
      dfs(x+1, i+1, sum+numList[i])


dfs(0, 0, 0)
print(cnt)
