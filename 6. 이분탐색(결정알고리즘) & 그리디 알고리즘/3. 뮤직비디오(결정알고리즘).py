import sys
filePath_laptop = "C:\\Users\khj77\\OneDrive\\바탕 화면\\Python\\python_Algo_practice\\Python-Algorithom\\6. 이분탐색(결정알고리즘) & 그리디 알고리즘\\input.txt"
filePath_desktop = "C:\\Users\\cywoo\\OneDrive\\바탕 화면\\Python\\python_algo_practice\\Python-Algorithom\\6. 이분탐색(결정알고리즘) & 그리디 알고리즘\\input.txt"
sys.stdin = open(filePath_desktop, "rt")

n, m = map(int, input().split())
dvd = list(map(int, input().split()))

maxTime = sum(dvd)
lt = 1
rt = maxTime
res = 0
while lt <= rt:
  mid = (lt + rt) // 2
  tmpSum = 0
  cnt = 0
  for x in dvd:
    tmpSum += x 
    if tmpSum >= mid:
      cnt += 1
      tmpSum = x
      # print(mid, cnt, tmpSum)

  if cnt == m:
    res = mid
    lt = mid + 1
  elif cnt < m:
    rt = mid - 1
  else:
    lt = mid + 1
  
print(res)
