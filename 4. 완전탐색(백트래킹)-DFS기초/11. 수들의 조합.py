# 상태트리 (가지가 여러개인 트리)
import sys
import itertools as it
filePath = "C:\\Users\khj77\\OneDrive\\바탕 화면\\Python\\python_Algo_practice\\Python-Algorithom\\4. 완전탐색(백트래킹)-DFS기초\\input.txt"
sys.stdin = open(filePath, "rt")

n, k = map(int, input().split())
numList = list(map(int, input().split()))
m = int(input())
cnt = 0
c = list(it.combinations(numList, k))

for x in c:
  res = sum(x)
  if res % m == 0:
    cnt += 1
print(cnt)