from collections import deque
import sys
filePath = "C:\\Users\khj77\\OneDrive\\바탕 화면\\Python\\python_Algo_practice\\Python-Algorithom\\5. 깊이,넓이 우선탐색 활용\\input.txt"
sys.stdin = open(filePath, "rt")

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]


# solution 추가
dx = [-1, 0 , 1, 0]
dy = [0, 1, 0, -1]
dq = deque()
dq.append((n//2, n//2)) # (x좌표, y좌표)
res = board[n//2][n//2]
check = [[0] * n for _ in range(n)]
check[n//2][n//2] = 1
level = 0

while True:
  if level == n//2:
    break
  size = len(dq)
  for i in range(size):
    now = dq.popleft()
    for j in range(4): # 시계방향으로 4번 수행
      x = now[0]+dx[j]
      y = now[1]+dy[j]
      if check[x][y] == 0:
        res += board[x][y]
        check[x][y] = 1
        dq.append((x, y))
  level += 1

print(res)


''' 첫번째 코드 -> 100점

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 0 , 1, 0]
dy = [0, 1, 0, -1]
dq = deque()
dq.append((n//2, n//2, 0)) # (x좌표, y좌표, level(depth))
res = board[n//2][n//2]
check = [[0] * n for _ in range(n)]
check[n//2][n//2] = 1

while dq:
  now = dq.popleft()
  if now[2] > n//2:
    break
  # print(now[0], now[1], now[2])
  for i in range(4):
    if n > now[0]+dx[i] >= 0 and n > now[1]+dy[i] >= 0 and now[2] < n//2:
      if check[now[0]+dx[i]][now[1]+dy[i]] == 0: 
        dq.append((now[0]+dx[i],now[1]+dy[i],now[2]+1))
        check[now[0]+dx[i]][now[1]+dy[i]] = 1
        res += board[now[0]+dx[i]][now[1]+dy[i]]
        # print(now[0]+dx[i], now[1]+dy[i], now[2]+1)
print(res)
'''