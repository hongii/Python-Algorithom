from collections import deque

n = int(input())
numList = deque(map(int, input().split()))

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