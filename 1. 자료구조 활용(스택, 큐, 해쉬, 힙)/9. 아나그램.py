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

'''
# solution
# 딕셔너리에서의 get 함수 -> dic.get("key", 0) : dic딕셔너리에 "key"값이 존재하면 그 key에 해당하는 value를 리턴하고, 해당 key가 없으면 0을 리턴한다.
a = input()
b = input()
str1 = dict()
str2 = dict()

for x in a:
	str1[x] = str1.get(x, 0) + 1

for x in b:
	str2[x] = str2.get(x, 0) + 1

if (str1 == str2):
	print("YES")
else:
	print("NO")
'''

'''
solution 개선된 코드

a = input()
b = input()
dicHash = dict()

for x in a:
	dicHash[x] = dicHash.get(x, 0) + 1

for x in b:
	dicHash[x] = dicHash.get(x, 0) - 1

for x in a:
	if (dicHash.get(x) > 0):
		print("NO")
		break
else:
	print("YES")
'''

