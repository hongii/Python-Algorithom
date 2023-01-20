import sys
# filePath = "C:\\Users\khj77\\OneDrive\\바탕 화면\\Python\\python_Algo_practice\\Python-Algorithom\\3. 탐색&시뮬레이션(string,1차원,2차원 리스트탐색)\\input.txt"
# sys.stdin = open(filePath, "rt")

numList = [i for i in range(0, 21)]
for i in range(10):
  a, b = map(int, input().split())
  tmp = numList[a:b+1]
  numList[a:b+1] = tmp[::-1]

for i in range(21):
  if i == 0:
    continue
  else:
    print(numList[i], end=" ")
