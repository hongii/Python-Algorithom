# 문제 설명 추가: 가장 마지막 행에서 시작해서 사다리의 왼쪽과 오른쪽을 먼저 보고 이동이 불가능하면 위로 올라가는 방식
import sys

board = [list(map(int, input().split())) for _ in range(10)]
check = [[0]*10 for _ in range(10)]
dy = [-1, 1]

def dfs(x, y):
  if x == 0 and board[x][y] == 1:
    print(y)
    sys.exit(0)
  else:
    for i in range(2):
      y_ = y + dy[i]
      if 0<=x<10 and 0<=y_<10 and board[x][y_] == 1 and check[x][y_] == 0:
        check[x][y_] = 1
        # print(1, (x, y_))
        dfs(x, y_)
        check[x][y_] = 0
    else:
      if 0<x<10 and 0<=y<10 and board[x-1][y] == 1 and check[x-1][y] == 0:
        check[x-1][y] = 1
        # print(2, (x-1, y))
        dfs(x-1, y)
        check[x-1][y] = 0

for i in range(10):
  if board[9][i] == 2:
    dfs(9, i)
    break