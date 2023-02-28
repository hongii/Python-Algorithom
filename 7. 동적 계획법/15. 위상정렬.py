'''
위상정렬 : 위상정렬은 어떤 일을 하는 순서를 찾는 알고리즘이다.
=>  각각의 일의 선후관계가 복잡하게 얽혀있을 때 각각 일의 선후관계를 유지하면서 
    전체 일의 순서를 짜는 알고리즘
    각 노드로 들어오는 방향의 간선의 갯수 : 진입 차수
    진입차수를 저장하는 리스트를 만들어야 한다.
'''

from collections import deque
import sys
filePath_laptop = "C:\\Users\khj77\\OneDrive\\바탕 화면\\Python\\python_Algo_practice\\Python-Algorithom\\7. 동적 계획법\\input.txt"
filePath_desktop = "C:\\Users\\cywoo\\OneDrive\\바탕 화면\\Python\\python_algo_practice\\Python-Algorithom\\7. 동적 계획법\\input.txt"
sys.stdin = open(filePath_desktop, "rt")

n, m = map(int, input().split())
graph = [[0]*(n+1) for _ in range(n+1)]
degree = [0]*(n+1)
dq = deque()

# 입력값을 받아서 진입차수 설정, 그래프 만들기
for i in range(m):
  v, w = map(int, input().split())
  degree[w] += 1
  graph[v][w] = 1
# print(degree)

# 진입차수 리스트에서 0인 i값(노드 번호)을 먼저 dq에 넣기
for i in range(1, n+1):
  if degree[i] == 0:
    dq.append(i)

# dq안에는 진입차수가 0인 노드만 들어있으므로, 해당 노드를 pop하고 나서 해당 노드에 의해 진입차수가 생성된 노드들을 찾아내 진입차수를 1 감소시킨다.
# 만약 연결된 노드의 진입차수를 1 감소한 후에 진입차수 값이 0이 되었다면, 그 노드 또한 dq에 넣어준다.
while dq:
  now = dq.popleft()
  print(now, end=" ")
  for idx, x in enumerate(graph[now]):
    if x == 1:
      degree[idx] -= 1
      if degree[idx] == 0:
        dq.append(idx)
