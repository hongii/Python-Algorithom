import sys
filePath = "C:\\Users\khj77\\OneDrive\\바탕 화면\\Python\\python_Algo_practice\\Python-Algorithom\\4. 완전탐색(백트래킹)-DFS기초\\input.txt"
sys.stdin = open(filePath, "rt")

n = int(input())
coins = list(map(int, input().split()))
coins.sort(reverse=True)
m = int(input())
minCnt = sys.maxsize

# solution
def dfs(x, res):
  global minCnt
  if res > m:
    return
  if x >= minCnt:
    return
  if res == m:
    if x < minCnt:
      minCnt = x
  else:
    for i in range(n):
      dfs(x+1, res+coins[i])


dfs(0, 0)
print(minCnt)

'''첫번째 코드 80점 -> 4번 테케 wrong answer
def dfs(x):
  global res;
  if res > m:
    return
  if res == m:
    print(x)
    sys.exit(0)
  else:
    for i in range(n):
      res += coins[i]
      print(res, i , x)
      dfs(x+1)
      res -= coins[i]

dfs(0)
'''