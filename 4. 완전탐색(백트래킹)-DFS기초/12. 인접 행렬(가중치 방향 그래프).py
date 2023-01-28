# 가중치 방향 그래프 -> 2차원 리스트로 인접행렬 구현
import sys
filePath = "C:\\Users\khj77\\OneDrive\\바탕 화면\\Python\\python_Algo_practice\\Python-Algorithom\\4. 완전탐색(백트래킹)-DFS기초\\input.txt"
sys.stdin = open(filePath, "rt")

n, m = map(int, input().split())
graph = [[0]*(n+1) for _ in range(n+1)]

# 가중치 방향 그래프 생성
for i in range(m):
  x, y, w = map(int, input().split())
  graph[x][y] = w


# 가중치 방향 그래프 출력
for i in range(1, n+1):
  for j in range(1, n+1):
    print(graph[i][j], end=" ")
  print()