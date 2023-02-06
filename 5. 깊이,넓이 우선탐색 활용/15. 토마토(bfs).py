from collections import deque
import sys
filePath_laptop = "C:\\Users\khj77\\OneDrive\\바탕 화면\\Python\\python_Algo_practice\\Python-Algorithom\\5. 깊이,넓이 우선탐색 활용\\input.txt"
filePath_desktop = "C:\\Users\\cywoo\\OneDrive\\바탕 화면\\Python\\python_algo_practice\\Python-Algorithom\\5. 깊이,넓이 우선탐색 활용\\input.txt"
sys.stdin = open(filePath_desktop, "rt")

m, n = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
days = 0
dq = deque()
check = [[0]*m for _ in range(n)]

# 이번 문제에서는 board[i][j] == 1인 부분들을 먼저 dq에 넣고 같은 level끼리 동시에 뻗어나가는 bfs로 구현해야 한다.
for i in range(n):
  for j in range(m):
    if board[i][j] == 1:
      dq.append((i, j , 0)) #(x좌표, y좌표, level)

while dq:
  now = dq.popleft()
  days = now[2]
  for k in range(4):
    x = now[0] + dx[k]
    y = now[1] + dy[k]
    l = now[2] + 1
    if 0 <= x < n and 0 <= y < m  and board[x][y] == 0:
      board[x][y] = 1
      dq.append((x, y, l))
      # print((x, y, l)) 
    
res = days
for i in range(n):
  if any(x== 0 for x in board[i]):
    res = -1
    break

print(res)


