# bfs 익히기
import sys
from collections import deque 
filePath = "C:\\Users\khj77\\OneDrive\\바탕 화면\\Python\\python_Algo_practice\\Python-Algorithom\\5. 깊이,넓이 우선탐색 활용\\input.txt"
sys.stdin = open(filePath, "rt")

s, e = map(int, input().split())
dq = deque()
dq.append(s)
distance = [-1] *(10001) # s점을 시작점으로 하여 각 index번호(node번호)까지 가는데 걸리는 거리 (가능한 좌표값: 1 ~ 10000까지)
distance[s] = 0 # 시작점은 거리가 0

while dq:
  now = dq.popleft()
  if now == e:
    break
  # 현재 노드로 부터 한칸 앞(now+1), 한칸 뒤로(now-1), 5칸 앞(now+5)씩 상태트리를 뻗어나간다.
  for next in(now-1, now+1, now+5): # next는 now-1, now+1, now+5 값 순서대로 반복문을 수행한다. 
    if 0 < next <= 10000: # 가능한 좌표점은 1 ~ 10000
      if distance[next] == -1:
        dq.append(next)
        distance[next] = distance[now] + 1 

print(distance[e])



