from itertools import permutations 
import sys
filePath = "C:\\Users\khj77\\OneDrive\\바탕 화면\\Python\\python_Algo_practice\\Python-Algorithom\\4. 완전탐색(백트래킹)-DFS기초\\input.txt"
sys.stdin = open(filePath, "rt")
n, m = map(int, input().split())
res = [0] * m
check = [0] * (n+1)
cnt = 0

'''solution -> check 배열을 만들어서 중복된 가지부분은 피하기'''
def dfs(x):
  global cnt, res
  if x == m:
    cnt += 1
    for i in range(m):
      print(res[i], end=" ")
    print()
  else:
    for i in range(1, n+1):
      if check[i] == 0:
        check[i] = 1
        res[x] = i
        dfs(x+1)
        check[i] = 0 #dfs(x+1)수행 후 돌아와서 다시 check[i]부분을 0으로 되돌려 놔야한다.


dfs(0)
print(cnt)


''' dfs 구현해서 풀어본 것
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
    
'''

''' itertools 라이브러리를 이용한 순열 구하기 연습
n, m = map(int, input().split())
numList = [i for i in range(1, n + 1)]

data = list(permutations(numList, m))
for x in data:
	print(*x)
print(len(data))
'''