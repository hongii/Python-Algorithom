### Queue 활용 ###
# <dequeue 라이브러리 사용>

# 다시 풀 문제 -> input2 예시에서 wrong answer

from collections import deque
import sys
filePath = "C:\\Users\khj77\\OneDrive\\바탕 화면\\Python\\python_Algo_practice\\Python-Algorithom\\1. 자료구조 활용(스택, 큐, 해쉬, 힙)\\input.txt"
sys.stdin = open(filePath, "rt")

necessary = input()
n = int(input())

for i in range(n):
	course = input()
	dq = deque(necessary)
	for x in course:
		if x in dq: # 현수가 계획한 과목이 필수과목에 해당하는지 확인
			if x != dq.popleft(): # 현수가 계획한 과목이 필수과목의 순서와 다른 경우
				print("#{0} {1}".format(i+1, "NO"))
				break
	else:
		if len(dq) == 0: # 필수과목과 현수가 계획한 과목에 모든 필수과목이 제대로 들어있고 그 순서까지 동일한 경우
			print("#{0} {1}".format(i+1, "YES"))
		else:  # 필수과목과 현수가 계획한 과목의 순서는 맞긴한데, 필수과목 중 일부가 빠져있는 경우 -> dq에 필수과목이 남아있는 상태
			print("#{0} {1}".format(i+1, "NO"))


'''
# 나는 과목 계획을 deque에 넣었는데, 필수과목을 deque에 넣고 푸는것으로 바꿔풀자.
necessary = input()
n = int(input())
course = []
for i in range(n):
	course.append(input())

for i in range(n):
	dq = deque(course[i])
	test = []
	for j in range(len(necessary)):
		for k in range(len(dq)):
			tmp = dq.popleft()
			if (necessary[j] == tmp):
				test.append(tmp)
				break
	print(test)
	if (len(test) != len(necessary)):
		print("#{0} {1}".format(i+1, "NO"))
	elif (test != list(necessary)):
		print("#{0} {1}".format(i+1, "NO"))
	else:
		print("#{0} {1}".format(i+1, "YES"))
'''
