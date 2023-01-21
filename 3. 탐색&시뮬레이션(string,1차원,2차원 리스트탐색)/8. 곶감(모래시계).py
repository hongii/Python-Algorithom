import sys
from collections import deque
filePath = "C:\\Users\khj77\\OneDrive\\바탕 화면\\Python\\python_Algo_practice\\Python-Algorithom\\3. 탐색&시뮬레이션(string,1차원,2차원 리스트탐색)\\input.txt"
sys.stdin = open(filePath, "rt")

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
m = int(input())
order = [list(map(int, input().split())) for _ in range(m)]

for x in order:
  tmp = deque(board[x[0]-1])
  if x[1] == 0:
    tmp.rotate(-x[2])
  elif x[1] == 1:
    tmp.rotate(x[2])
  board[x[0]-1] = list(tmp)

sum = 0
l,r = 0, n-1
for i in range(n):
  for j in range(l, r+1):
    sum += board[i][j]
  if i < n//2:
    l += 1
    r -= 1
  else:
    l -= 1
    r += 1
print(sum)