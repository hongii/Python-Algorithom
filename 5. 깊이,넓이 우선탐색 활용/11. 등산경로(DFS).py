import sys
filePath = "C:\\Users\khj77\\OneDrive\\바탕 화면\\Python\\python_Algo_practice\\Python-Algorithom\\5. 깊이,넓이 우선탐색 활용\\input.txt"
sys.stdin = open(filePath, "rt")

n = int(input())
board = [list(map(int, input().split())) for i in range(n)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
check = [[0]*n for _ in range(n)]
cnt = 0

minNum = board[0][0]
maxNum = board[0][0]
start, end = (0, 0), (0, 0)
for i in range(n):
  if minNum > min(board[i]):
    minNum = min(board[i])
    start = (i, board[i].index(min(board[i])))
  if maxNum < max(board[i]):
    maxNum = max(board[i])
    end = (i, board[i].index(max(board[i])))
check[start[0]][start[1]] = 1

def dfs(node):
  global cnt
  if node == end:
    cnt += 1
  else:
    for i in range(4):
      x = node[0] + dx[i]
      y = node[1] + dy[i]
      if 0 <= x < n and 0 <= y < n and check[x][y] == 0 and board[x][y] > board[node[0]][node[1]]:
        check[x][y] = 1
        dfs((x, y))
        check[x][y] = 0
        
dfs(start)
print(cnt)