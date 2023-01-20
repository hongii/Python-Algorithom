import sys
filePath = "C:\\Users\khj77\\OneDrive\\바탕 화면\\Python\\python_Algo_practice\\Python-Algorithom\\3. 탐색&시뮬레이션(string,1차원,2차원 리스트탐색)\\input.txt"
sys.stdin = open(filePath, "rt")

n = int(input())
board = [[0] * n for i in range(n)]
sumMax = 0
for i in range(n):
  board[i] = list(map(int, input().split()))
  sumRow = sum(board[i])
  if sumRow > sumMax:
    sumMax = sumRow

for i in range(n):
	sumCol = 0
	for j in range(n):
		sumCol += board[j][i]
	if sumCol > sumMax:
		sumMax = sumCol

sumDiagonal = 0
for i in range(n):
	sumDiagonal += board[i][i]
else:
	if sumDiagonal > sumMax:
		sumMax = sumDiagonal

print(sumMax)
