# 다시 풀어볼 문제 -> 아이디어 생각 못함 : board를 이중 for문으로 돌면서 dfs수행
import sys
filePath = "C:\\Users\khj77\\OneDrive\\바탕 화면\\Python\\python_Algo_practice\\Python-Algorithom\\5. 깊이,넓이 우선탐색 활용\\input.txt"
sys.stdin = open(filePath, "rt")

n = int(input())
board = [list(map(int, input())) for _ in range(n)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
# check = [[0]*n for _ in range(n)] # 이번엔 check배열을 사용하지 않고, 이미 거쳐온 경로면  board 리스트 요소 값을 1에서 0으로 바꾸는 방식으로 check할거임
res = []
cnt = 1

def dfs(node):
  global cnt
  board[node[0]][node[1]] = 0
  for i in range(4):
    x = node[0] + dx[i]
    y = node[1] + dy[i]
    if 0<=x<n and 0<=y<n and board[x][y] == 1:
      cnt += 1
      board[node[0]][node[1]] = 0
      dfs((x, y))

for i in range(n):
  for j in range(n):
    if board[i][j] == 1:
      dfs((i,j))
      res.append(cnt)
      cnt = 1

print(len(res))
res.sort()
for x in res:
  print(x)