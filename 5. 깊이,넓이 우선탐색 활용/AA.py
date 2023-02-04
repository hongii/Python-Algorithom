n = int(input())
board = [list(map(int, input())) for _ in range(n)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
res = []
cnt = 1


def dfs(node):
  global cnt
  board[node[0]][node[1]] = 0
  for i in range(4):
    x = node[0] + dx[i]
    y = node[1] + dy[i]
    if 0 <= x < n and 0 <= y < n and board[x][y] == 1:
      cnt += 1
      board[node[0]][node[1]] = 0
      dfs((x, y))


for i in range(n):
  for j in range(n):
    if board[i][j] == 1:
      dfs((i, j))
      res.append(cnt)
      cnt = 1

print(len(res))
res.sort()
for x in res:
  print(x)
