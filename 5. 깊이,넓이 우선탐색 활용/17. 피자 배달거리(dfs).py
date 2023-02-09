# 문제 이해를 제대로 못했음 -> 다시 풀어볼 문제(조합이용)
import itertools as it 
import sys
filePath_laptop = "C:\\Users\khj77\\OneDrive\\바탕 화면\\Python\\python_Algo_practice\\Python-Algorithom\\5. 깊이,넓이 우선탐색 활용\\input.txt"
filePath_desktop = "C:\\Users\\cywoo\\OneDrive\\바탕 화면\\Python\\python_algo_practice\\Python-Algorithom\\5. 깊이,넓이 우선탐색 활용\\input.txt"
sys.stdin = open(filePath_desktop, "rt")

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
pizza = []
house = []

# 피자집(board[i][j] == 2)과 집(board[i][j] == 1)인 좌표를 각각 pizza와 house 리스트에 담기
for i in range(n):
  for j in range(n):
    if board[i][j] == 2: # 피자집 좌표 담기
      pizza.append((i, j))
    elif board[i][j] == 1: # 집의 좌표 담기
      house.append((i, j))

pizza_idx = [i for i in range(len(pizza))]  
cb = list(it.combinations(pizza_idx, m)) # 피자집 m개를 고르는 조합
# print(cb)

res = sys.maxsize
for i in range(len(cb)):
  p = cb[i]
  totalDistance = 0
  for j in range(len(house)):
    minDistance = sys.maxsize
    for k in p:
      x = abs(house[j][0] - pizza[k][0])
      y = abs(house[j][1] - pizza[k][1])
      if x + y < minDistance:
        minDistance = x + y
    totalDistance += minDistance
  if totalDistance < res:
    res = totalDistance

print(res)




