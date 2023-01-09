# 딕셔너리 

import sys
filePath = "C:\\Users\khj77\\OneDrive\\바탕 화면\\Python\\python_Algo_practice\\Python-Algorithom\\1. 자료구조 활용(스택, 큐, 해쉬, 힙)\\input.txt"
sys.stdin = open(filePath, "rt")

n = int(input())
words = []
for i in range(n):
	words.append(input())

for i in range(n-1):
	word = input()
	if word in words:
		popIdx = words.index(word)
		words.pop(popIdx)
print(words[0])

'''
# solution : dictionary 사용하기
# 노트에 적어둔 단어(key)의 value 값을 1로 초기화하고, 노트에 쓰여진 단어의 value값을 0으로 수정하고 마지막에 value가 1인 단어 하나를 출력시키면 된다.
n = int(input())
words = dict()
for i in range(n):
	word = input()
	words[word] = 1

for i in range(n-1):
	word = input()
	words[word] = 0

for key, val in words.items():
	if(val == 1):	
		print(key)
		break
'''