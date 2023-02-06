from collections import deque

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