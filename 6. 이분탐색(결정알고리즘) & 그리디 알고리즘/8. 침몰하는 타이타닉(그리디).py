# list대신 deque를 쓰면 시간 복잡도 효율을 높일 수 있다. -> deque의 경우 popleft()하면 맨 처음 원소를 가리키는 포인터 위치만 한칸 뒤로 바뀌는 것이므로 시간복잡도가 O(1), list의 경우에는 앞으로 한칸씩 모든 원소가 이동하므로 시간복잡도가 O(n)이 된다.
from collections import deque
import sys
filePath_laptop = "C:\\Users\khj77\\OneDrive\\바탕 화면\\Python\\python_Algo_practice\\Python-Algorithom\\6. 이분탐색(결정알고리즘) & 그리디 알고리즘\\input.txt"
filePath_desktop = "C:\\Users\\cywoo\\OneDrive\\바탕 화면\\Python\\python_algo_practice\\Python-Algorithom\\6. 이분탐색(결정알고리즘) & 그리디 알고리즘\\input.txt"
sys.stdin = open(filePath_desktop, "rt")

n, m = map(int, input().split())
weight = deque(map(int, input().split()))
weight.sort()
cnt = 0

while weight:
  if len(weight) == 1:
    cnt += 1
    break
  # 가장 무거운 승객과 가장 가벼운 승객의 몸무게 합이 m을 초과하는 경우, 가장 무거운 승객만 구조된다.
  if weight[0] + weight[-1] > m:
    weight.pop()
    cnt += 1

  # 가장 무거운 승객과 가장 가벼운 승객의 몸무게 합이 m이하라면 두명이 함께 구조된다.
  else:
    weight.pop()
    weight.popleft()
    cnt += 1

''' 첫번째 코드 100점 -> 반복적으로 max함수 호출 : O(N)이므로 시간효율성이 떨어짐
while weight:
  remainder = m - weight[0]
  tmp, tmpIdx = -1, -1 
  for j in range(1, len(weight)):
    if remainder >= weight[j]:
      tmp = max(weight[j], tmp)
      tmpIdx = j

  # tmpIdx가 초기값 -1이 아니라면, 같이 구조되는 승객이 있다는 뜻
  if tmpIdx != -1:
    weight.pop(tmpIdx) # 같이 구조되는 승객 제거
  weight.pop(0) # 현재 구조되는 승객 제거
  cnt += 1
'''
print(cnt)