import sys
filePath = "C:\\Users\khj77\\OneDrive\\바탕 화면\\Python\\python_Algo_practice\\Python-Algorithom\\3. 탐색&시뮬레이션(string,1차원,2차원 리스트탐색)\\input.txt"
sys.stdin = open(filePath, "rt")

n = int(input())
nList = list(map(int, input().split()))
m = int(input())
mList = list(map(int, input().split()))
sortedList = list()

for i in range(n+m):
  if len(nList) == 0:
    sortedList.append(mList)
    break
  elif len(mList) == 0:
    sortedList.append(nList)
    break
  
  nListMin = nList[0]
  mListMin = mList[0]
  if nListMin < mListMin:
    sortedList.append(nListMin)
    nList.pop(0)
  else:
    sortedList.append(mListMin)
    mList.pop(0)
    
for x in sortedList:
  if type(x) is list:
    print(*x)  #Python 리스트에 Asterisk(*) 를 사용하면 리스트 압축 해제를 할 수 있게 된다. 즉, 리스트 대괄호를 생략하고 출력이 가능하다.
  else:
    print(x, end=" ")
