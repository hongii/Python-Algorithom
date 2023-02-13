import sys
filePath_laptop = "C:\\Users\khj77\\OneDrive\\바탕 화면\\Python\\python_Algo_practice\\Python-Algorithom\\6. 이분탐색(결정알고리즘) & 그리디 알고리즘\\input.txt"
filePath_desktop = "C:\\Users\\cywoo\\OneDrive\\바탕 화면\\Python\\python_algo_practice\\Python-Algorithom\\6. 이분탐색(결정알고리즘) & 그리디 알고리즘\\input.txt"
sys.stdin = open(filePath_desktop, "rt")

k, n = map(int, input().split())
numList = [int(input()) for _ in range(k)]

maxLen = max(numList)
lt = 1
rt = maxLen
res = 0

while lt <= rt:
  mid = (lt + rt) // 2
  total = 0
  for x in numList:
    total += x // mid

  if total >= n:
    res = mid 
    lt = mid + 1
  elif total < n:
    rt = mid - 1

print(res)