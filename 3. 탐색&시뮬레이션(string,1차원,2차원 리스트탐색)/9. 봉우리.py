import sys
filePath = "C:\\Users\khj77\\OneDrive\\바탕 화면\\Python\\python_Algo_practice\\Python-Algorithom\\3. 탐색&시뮬레이션(string,1차원,2차원 리스트탐색)\\input.txt"
sys.stdin = open(filePath, "rt")

n = int(input())
board = [[0]*(n+2) for i in range(n+2)]
for i in range(n):
  numList = list(map(int, input().split()))
  board[i+1][1:-1] = numList
# print(board)

cnt = 0
for i in range(1, n+1):
  for j in range(1, n+1):
    if board[i][j] > board[i-1][j] and board[i][j] > board[i][j-1] and board[i][j] > board[i][j+1] and board[i][j] > board[i+1][j]:
      cnt += 1
print(cnt)
