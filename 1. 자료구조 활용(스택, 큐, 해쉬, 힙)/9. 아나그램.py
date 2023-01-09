# 딕셔너리 해쉬
import sys
filePath = "C:\\Users\khj77\\OneDrive\\바탕 화면\\Python\\python_Algo_practice\\Python-Algorithom\\1. 자료구조 활용(스택, 큐, 해쉬, 힙)\\input.txt"
sys.stdin = open(filePath, "rt")

str1 = list(input())
str2 = list(input())
dic1 = {}
dic2 = {}

for i in range(len(str1)):
	if(str1[i] in dic1.keys()):
		dic1[str1[i]] += 1
	else:
		dic1[str1[i]] = 1
		
for i in range(len(str2)):
	if (str2[i] in dic2.keys()):
		dic2[str2[i]] += 1
	else:
		dic2[str2[i]] = 1

if (dic1==dic2):
	print("YES")
else:
	print("NO")
