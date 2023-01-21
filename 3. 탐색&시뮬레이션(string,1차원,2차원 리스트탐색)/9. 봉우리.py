import sys
filePath = "C:\\Users\khj77\\OneDrive\\바탕 화면\\Python\\python_Algo_practice\\Python-Algorithom\\3. 탐색&시뮬레이션(string,1차원,2차원 리스트탐색)\\input.txt"
sys.stdin = open(filePath, "rt")

n = int(input())
board = [[0]*(n+2) for _ in range(n+2)]
for i in range(n):
  numList = list(map(int, input().split()))
  board[i+1][1:-1] = numList
# print(board)

'''solution 참고: dx, dy 배열을 만들어서 상우하좌(시계방향) 값을 비교'''
cnt = 0
dx = [-1, 0, 1, 0] #index i에 더할 값
dy = [0, 1, 0, -1] #index j에 더할 값
for i in range(1, n+1):
  for j in range(1, n+1):
    if all(board[i][j] > board[i+dx[k]][j+dy[k]] for k in range(4)): #all()함수: 괄호안의 조건문이 모두 만족된다면 if문 통과
      cnt += 1


''' 상하좌우 값을 and로 하나하나 비교한 내 코드
cnt = 0
for i in range(1, n+1):
  for j in range(1, n+1):
    if board[i][j] > board[i-1][j] and board[i][j] > board[i][j-1] and board[i][j] > board[i][j+1] and board[i][j] > board[i+1][j]:
      cnt += 1
print(cnt)
'''