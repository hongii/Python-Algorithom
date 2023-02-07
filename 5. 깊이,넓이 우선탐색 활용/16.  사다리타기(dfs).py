# 문제 설명 추가: 가장 마지막 행에서 시작해서 사다리의 왼쪽과 오른쪽을 먼저 보고 이동이 불가능하면 위로 올라가는 방식
import sys
filePath_laptop = "C:\\Users\khj77\\OneDrive\\바탕 화면\\Python\\python_Algo_practice\\Python-Algorithom\\5. 깊이,넓이 우선탐색 활용\\input.txt"
filePath_desktop = "C:\\Users\\cywoo\\OneDrive\\바탕 화면\\Python\\python_algo_practice\\Python-Algorithom\\5. 깊이,넓이 우선탐색 활용\\input.txt"
sys.stdin = open(filePath_desktop, "rt")

board = [list(map(int, input().split())) for _ in range(10)]
check = [[0]*10 for _ in range(10)]

def dfs(x, y):
  if x == 0 and board[x][y] == 1:
    print(y)
  else:
    if 0<=x<10 and 0<= y-1 <10 and board[x][y-1] == 1 and check[x][y-1] == 0:
      check[x][y-1] = 1
      dfs(x, y-1)
      check[x][y-1] = 0
    elif 0<=x<10 and 0<= y+1 <10 and board[x][y+1] == 1 and check[x][y+1] == 0:
      check[x][y+1] = 1
      dfs(x, y+1)
      check[x][y+1] = 0
    else:   
      check[x-1][y] = 1
      dfs(x-1, y)
      check[x-1][y] = 0

for i in range(10):
  if board[9][i] == 2:
    dfs(9, i)
    break