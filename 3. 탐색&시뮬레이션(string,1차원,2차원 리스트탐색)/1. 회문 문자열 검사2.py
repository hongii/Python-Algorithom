# 복습-2회차
import sys
filePath_laptop = "C:\\Users\khj77\\OneDrive\\바탕 화면\\Python\\python_Algo_practice\\Python-Algorithom\\3. 탐색&시뮬레이션(string,1차원,2차원 리스트탐색)\\input.txt"
filePath_desktop = "C:\\Users\\cywoo\\OneDrive\\바탕 화면\\Python\\python_algo_practice\\Python-Algorithom\\3. 탐색&시뮬레이션(string,1차원,2차원 리스트탐색)\\input.txt"
sys.stdin = open(filePath_desktop, "rt")

n = int(input())
words = [input().lower() for _ in range(n)]

w1, w2 = "",  ""
for i in range(len(words)):
  midIdx = len(words[i]) // 2
  w1 = words[i][:midIdx]
  w2 = words[i][midIdx:][::-1]
  if len(words[i]) % 2 == 1:
    w2 = words[i][midIdx+1:][::-1]

  if w1 == w2:
    print("#{0} YES".format(i+1))
  else:
    print("#{0} NO".format(i+1))

