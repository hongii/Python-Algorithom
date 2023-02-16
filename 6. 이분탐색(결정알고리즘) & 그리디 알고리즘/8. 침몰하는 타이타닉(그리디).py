import sys
filePath_laptop = "C:\\Users\khj77\\OneDrive\\바탕 화면\\Python\\python_Algo_practice\\Python-Algorithom\\6. 이분탐색(결정알고리즘) & 그리디 알고리즘\\input.txt"
filePath_desktop = "C:\\Users\\cywoo\\OneDrive\\바탕 화면\\Python\\python_algo_practice\\Python-Algorithom\\6. 이분탐색(결정알고리즘) & 그리디 알고리즘\\input.txt"
sys.stdin = open(filePath_desktop, "rt")

n, m = map(int, input().split())
weight = list(map(int, input().split()))
weight.sort()
cnt = 0
while weight:
  remainder = m - weight[0]
  tmp, tmpIdx = -1, -1 
  for j in range(1, len(weight)):
    if remainder >= weight[j]:
      tmp = max(weight[j], tmp)
      tmpIdx = j

  # tmpIdx가 초기값-1이 아니라면, 같이 구조되는 승객이 있다는 뜻
  if tmpIdx != -1:
    weight.pop(tmpIdx) # 같이 구조되는 승객 제거
  weight.pop(0) # 현재 구조되는 승객 제거
  cnt += 1

print(cnt)