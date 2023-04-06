from collections import deque
import sys
filePath_laptop = "C:\\Users\khj77\\OneDrive\\바탕 화면\\Python\\python_Algo_practice\\Python-Algorithom\\6. 이분탐색(결정알고리즘) & 그리디 알고리즘\\input.txt"
filePath_desktop = "C:\\Users\\cywoo\\OneDrive\\바탕 화면\\Python\\python_algo_practice\\Python-Algorithom\\6. 이분탐색(결정알고리즘) & 그리디 알고리즘\\input.txt"
sys.stdin = open(filePath_desktop, "rt")


# 2회차 복습 풀이 -> 100점
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



'''
# solution 참고
lt, rt = 0, n-1
lastNum = 0
comp = []
res = ""
while lt <= rt:
  # lastNum과 numList의 왼쪽 오른쪽 양쪽값을 각각 비교해서 numList값이 더 크다면 comp 리스트에 추가
  if lastNum < numList[lt]:
    comp.append((numList[lt], "L"))
  if lastNum < numList[rt]:
    comp.append((numList[rt], "R"))

# 튜플의 1번째 원소값 기준으로 오름차순 정렬
  comp.sort()

  if len(comp) == 0: # comp 리스트에 아무 원소도 안들어 간 경우
    break
  else:
    res += comp[0][1]
    lastNum = comp[0][0]

    # lt와 rt가 가르키는 위치 갱신
    if comp[0][1] == "L":
      lt += 1
    else:
      rt -= 1
  comp.clear()

print(len(res))
print(res)
'''

'''첫번째 코드 100점
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
'''