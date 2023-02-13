import sys
filePath_laptop = "C:\\Users\khj77\\OneDrive\\바탕 화면\\Python\\python_Algo_practice\\Python-Algorithom\\6. 이분탐색(결정알고리즘) & 그리디 알고리즘\\input.txt"
filePath_desktop = "C:\\Users\\cywoo\\OneDrive\\바탕 화면\\Python\\python_algo_practice\\Python-Algorithom\\6. 이분탐색(결정알고리즘) & 그리디 알고리즘\\input.txt"
sys.stdin = open(filePath_desktop, "rt")
n, m  = map(int, input().split())
numList = list(map(int, input().split()))
numList.sort()
lt = 0
rt = n - 1

while lt <= rt:
  mid = (lt + rt) // 2
  if numList[mid] == m:
    print(mid + 1)
    break
  elif numList[mid] < m:
    lt = mid + 1
  elif numList[mid] > m:
    rt = mid - 1


