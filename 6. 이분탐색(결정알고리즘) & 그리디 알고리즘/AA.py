from collections import deque
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
