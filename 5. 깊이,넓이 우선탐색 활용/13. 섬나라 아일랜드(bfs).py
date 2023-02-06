from collections import deque
import sys
filePath_laptop = "C:\\Users\khj77\\OneDrive\\바탕 화면\\Python\\python_Algo_practice\\Python-Algorithom\\5. 깊이,넓이 우선탐색 활용\\input.txt"
filePath_desktop = "C:\\Users\\cywoo\\OneDrive\\바탕 화면\\Python\\python_algo_practice\\Python-Algorithom\\5. 깊이,넓이 우선탐색 활용\\input.txt"
sys.stdin = open(filePath_desktop, "rt")

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]
cnt = 0
dq = deque()

for i in range(n):
  for j in range(n):
    if board[i][j] == 1:
      board[i][j] = 0
      dq.append((i, j))
      cnt += 1
      while dq:
        now = dq.popleft()
        for k in range(8):
          x = now[0] + dx[k]
          y = now[1] + dy[k]
          if 0 <= x < n and 0 <= y < n and board[x][y] == 1:
            board[x][y] = 0
            dq.append((x, y))
            

print(cnt)