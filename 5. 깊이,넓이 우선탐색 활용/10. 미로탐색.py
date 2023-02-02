from collections import deque
import sys
filePath = "C:\\Users\khj77\\OneDrive\\바탕 화면\\Python\\python_Algo_practice\\Python-Algorithom\\5. 깊이,넓이 우선탐색 활용\\input.txt"
sys.stdin = open(filePath, "rt")

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
board = [list(map(int, input().split())) for _ in range(7)]
dq = deque()
dq.append((0, 0))
cnt = 0
check = [[0]*7 for _ in range(7)]
check[0][0] = 1

def dfs(x, y):
  global cnt
  if x == 6 and y == 6:
    cnt += 1
  else:
    for i in range(4):
      x2 = x + dx[i]
      y2 = y + dy[i]
      if 0 <= x2 < 7 and 0 <= y2 < 7 and check[x2][y2] == 0 and board[x2][y2] == 0:
        check[x2][y2] = 1
        dfs(x2, y2)
        check[x2][y2] = 0
dfs(0, 0)
print(cnt)
