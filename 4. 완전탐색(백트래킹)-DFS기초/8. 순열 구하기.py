from itertools import permutations 
import sys
filePath = "C:\\Users\khj77\\OneDrive\\바탕 화면\\Python\\python_Algo_practice\\Python-Algorithom\\4. 완전탐색(백트래킹)-DFS기초\\input.txt"
sys.stdin = open(filePath, "rt")
n, m = map(int, input().split())
res = [0] * m
cnt = 0

def dfs(x):
  global cnt, res
  if x == m:
    tmpRes = sorted(res)
    setRes = sorted(list(set(res)))
    if tmpRes == setRes:
      cnt += 1
      for i in range(m):
        print(res[i], end = " ")
      print()
  else:
    for i in range(1, n+1):
      res[x] = i
      dfs(x+1)
dfs(0)
print(cnt)
    


''' itertools 라이브러리를 이용한 순열 구하기 연습
n, m = map(int, input().split())
numList = [i for i in range(1, n + 1)]

data = list(permutations(numList, m))
for x in data:
	print(*x)
print(len(data))
'''