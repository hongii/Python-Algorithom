from collections import deque
import sys
filePath_laptop = "C:\\Users\khj77\\OneDrive\\바탕 화면\\Python\\python_Algo_practice\\Python-Algorithom\\6. 이분탐색(결정알고리즘) & 그리디 알고리즘\\input.txt"
filePath_desktop = "C:\\Users\\cywoo\\OneDrive\\바탕 화면\\Python\\python_algo_practice\\Python-Algorithom\\6. 이분탐색(결정알고리즘) & 그리디 알고리즘\\input.txt"
sys.stdin = open(filePath_desktop, "rt")

n = int(input())
numList = deque(map(int, input().split()))

res = []
tmp = []
flagL, flagR = 0, 0
while numList:
  if len(numList) == 1:
    if tmp[-1] < numList[0]:
      res.append("L")
      tmp.append(numList[0])
      numList.pop()
      break
    else:
      break
  if numList[0] < numList[-1]:
    if len(tmp) > 0 and tmp[-1] > numList[0]:
      flagL = 1
      if tmp[-1] < numList[-1]:
        res.append("R")
        tmp.append(numList[-1])
        numList.pop()
      else:
        break
    else:
      res.append("L")
      tmp.append(numList[0])
      numList.popleft()
  elif numList[0] > numList[-1]: 
    if len(tmp) and tmp[-1] > numList[-1]:
      flagR = 1
      if tmp[-1] < numList[0]:
        res.append("L")
        tmp.append(numList[0])
        numList.popleft()
      else:
        break
    else:
      res.append("R")
      tmp.append(numList[-1])
      numList.pop()
  if flagL == flagR == 1:
    break

print(len(res))
for x in res:
  print(x, end="")
