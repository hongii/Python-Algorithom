import sys
filePath = "C:\\Users\khj77\\OneDrive\\바탕 화면\\Python\\python_Algo_practice\\Python-Algorithom\\3. 탐색&시뮬레이션(string,1차원,2차원 리스트탐색)\\input.txt"
sys.stdin = open(filePath, "rt");

n = int(input())
words = list()
for i in range(n):
  words.append(input())

cnt = 1
for word in words:
  word = word.lower()
  for i in range(len(word)):
    compLeft = word[i]
    compRight = word[len(word)-1-i]
    if compLeft != compRight:
      print("#{0} NO".format(cnt))
      cnt += 1 
      break
  else:
    print("#{0} YES".format(cnt))
    cnt += 1
