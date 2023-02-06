from collections import deque
import sys
filePath_laptop = "C:\\Users\khj77\\OneDrive\\바탕 화면\\Python\\python_Algo_practice\\Python-Algorithom\\5. 깊이,넓이 우선탐색 활용\\input.txt"
filePath_desktop = "C:\\Users\\cywoo\\OneDrive\\바탕 화면\\Python\\python_algo_practice\\Python-Algorithom\\5. 깊이,넓이 우선탐색 활용\\input.txt"
sys.stdin = open(filePath_desktop, "rt")

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
res = []
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
dq = deque()
maxHeight = 0
for i in range(n):
  tmpMax = max(board[i])
  if tmpMax > maxHeight:
    maxHeight = tmpMax
print(maxHeight)
for h in range(1, 101):
  if h == maxHeight:
    break
  else:
    safeZone = [[0]*n for _ in range(n)]

    # 높이가 h보다 큰 지역만 check(안전지대)
    for i in range(n):
      for j in range(n):
        if board[i][j] > h:
          safeZone[i][j] = 1
    
    # 안전지대 영역 탐색
    check = [[0]*n for _ in range(n)]
    cnt = 0
    for i in range(n):
      for j in range(n):
        if safeZone[i][j] == 1 and check[i][j] == 0:
          dq.append((i, j))
          check[i][j] = 1
          cnt += 1
          while dq:
            now = dq.popleft()
            for k in range(4):
              x = now[0] + dx[k]
              y = now[1] + dy[k]
              if 0 <= x < n and 0 <= y < n  and check[x][y] == 0 and safeZone[x][y] == 1:
                dq.append((x, y))
                check[x][y] = 1		
    res.append(cnt) # 장마철에 잠기는 높이에 따른 안전지대 영역 갯수
# print(res)
print(max(res))