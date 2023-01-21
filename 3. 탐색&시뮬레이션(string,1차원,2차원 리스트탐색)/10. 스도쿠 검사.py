import sys
filePath = "C:\\Users\khj77\\OneDrive\\바탕 화면\\Python\\python_Algo_practice\\Python-Algorithom\\3. 탐색&시뮬레이션(string,1차원,2차원 리스트탐색)\\input.txt"
sys.stdin = open(filePath, "rt")

board = [list(map(int, input().split())) for _ in range(9)]

numSet = {1, 2, 3, 4, 5, 6, 7, 8, 9}
check = 0
for i in range(9):
  col = []
  for j in range(9):
    col.append(board[j][i])
  if set(board[i]) == numSet and set(col) == numSet: #행과 열만 먼저 비교
    check = 1  

for i in range(0, 9, 3):
  triple = []
  for j in range(3):
    triple.extend(board[j][i:i+3])
    # print(board[j][i:i+3])
  if set(triple) != numSet:
    check = 0
    break
  
  triple = []
  for j in range(3, 6):
    triple.extend(board[j][i:i+3])
    # print(board[j][i:i+3])
  if set(triple) != numSet:
    check = 0
    break
  
  triple = []
  for j in range(6, 9):
    triple.extend(board[j][i:i+3])
    # print(board[j][i:i+3])
  if set(triple) != numSet:
    check = 0
    break

if check == 1:
	print("YES")
else:
  print("NO")