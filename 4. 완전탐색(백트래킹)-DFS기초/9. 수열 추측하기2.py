import sys
filePath = "C:\\Users\khj77\\OneDrive\\바탕 화면\\Python\\python_Algo_practice\\Python-Algorithom\\4. 완전탐색(백트래킹)-DFS기초\\input.txt"
sys.stdin = open(filePath, "rt")
n, f = map(int, input().split())
c = [0] * n
p = [0] * n
check = [0] * (n+1)

def factorial(x):
  sum = 1
  for i in range(1, x+1):
    sum *= i
  return sum

def dfs(x, sum):
  if x == n and sum == f:
    for x in p:
      print(x, end=" ")
    sys.exit(0)
  else:
    for i in range(1, n+1):
      if check[i] == 0:
        check[i] = 1
        p[x] = i
        dfs(x+1, sum + (p[x]*c[x]))
        check[i] = 0

# n의 값에 따른 이항계수 배열 생성 (n=4라면 배열 c에는 [1,3,3,1], n=5라면 [1,4,6,4,1]이 들어간다.)
for i in range(n):
  c[i] = factorial(n-1) // (factorial(n-1 - i) * factorial(i))

dfs(0, 0)