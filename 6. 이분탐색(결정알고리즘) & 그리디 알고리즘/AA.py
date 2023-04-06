from collections import deque
n = int(input())
numList = deque(map(int, input().split()))
pre = 0
res = ""
while len(numList) > 1:
  if pre < max(numList[0], numList[-1]):
    if numList[0] < numList[-1] and pre < numList[0]:
      pre = numList.popleft()
      res += "L"
    elif numList[0] < numList[-1] and pre > numList[0]:
      pre = numList.pop()
      res += "R"
    elif numList[0] > numList[-1] and pre < numList[-1]:
      pre = numList.pop()
      res += "R"
    elif numList[0] > numList[-1] and pre > numList[-1]:
      pre = numList.popleft()
      res += "L"
  else:
    break


if len(numList) == 1 and numList[0] > pre:
  res += "L"

print(len(res))
print(res)