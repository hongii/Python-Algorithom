import sys
filePath = "C:\\Users\khj77\\OneDrive\\바탕 화면\\Python\\python_Algo_practice\\Python-Algorithom\\3. 탐색&시뮬레이션(string,1차원,2차원 리스트탐색)\\input.txt"
sys.stdin = open(filePath, "rt")

board = [list(map(int, input().split())) for _ in range(7)]
cnt = 0

# 행 방향 회문수 비교
for i in range(7):
  for j in range(3):
    tmp = board[i][j:j+5]
    if tmp[0] == tmp[-1] and tmp[1] == tmp[-2]:
      cnt += 1

# 열 방향 회문수 비교
for i in range(7):
  for j in range(3):
    tmp = []
    for k in range(5):
      tmp.append(board[k+j][i])
    if tmp[0] == tmp[-1] and tmp[1] == tmp[-2]:
      cnt += 1

print(cnt)