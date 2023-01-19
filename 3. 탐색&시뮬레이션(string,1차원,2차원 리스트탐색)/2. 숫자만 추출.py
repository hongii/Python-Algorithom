import sys
filePath = "C:\\Users\khj77\\OneDrive\\바탕 화면\\Python\\python_Algo_practice\\Python-Algorithom\\3. 탐색&시뮬레이션(string,1차원,2차원 리스트탐색)\\input.txt"
sys.stdin = open(filePath, "rt")
str = input()

numStr = ""
for i in range(len(str)):
  if str[i].isdecimal():
    numStr += str[i]
else:
  res = int(numStr)
print(res)

cnt = 0
for i in range(1, res+1):
  if(res % i == 0):
    cnt += 1
print(cnt)