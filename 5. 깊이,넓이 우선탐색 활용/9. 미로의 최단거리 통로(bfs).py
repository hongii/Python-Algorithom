from collections import deque
import sys
filePath = "C:\\Users\khj77\\OneDrive\\바탕 화면\\Python\\python_Algo_practice\\Python-Algorithom\\5. 깊이,넓이 우선탐색 활용\\input.txt"
sys.stdin = open(filePath, "rt")

board = [list(map(int, input().split())) for _ in range(7)]
dq = deque()
dq.append((0, 0))  # 출발지점 (x, y)좌표 -> (0, 0)
distance = [[-1] * 7 for _ in range(7)]
distance[0][0] = 0
check = [[0]*7 for _ in range(7)]
check[0][0] = 1
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

while dq:
	size = len(dq)
	now = dq.popleft()
	# print(now)
	for i in range(size):
		for j in range(4):
			x = now[0] + dx[j]
			y = now[1] + dy[j]
			if 7 > x >= 0 and 7 > y >= 0 and board[x][y] == 0 and check[x][y] == 0:
				check[x][y] = 1
				# print(x, y)
				dq.append((x, y))
				distance[x][y] = distance[now[0]][now[1]] + 1

print(distance[6][6])
