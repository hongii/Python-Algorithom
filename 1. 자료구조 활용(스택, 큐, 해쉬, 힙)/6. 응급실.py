### Queue 활용 ###
# <dequeue 라이브러리 사용>

# 다시 볼 포인트 
# -> tuple쌍을 원소로 가지는 리스트 만드는 법
# -> max()함수에서 key값 설정해서 비교하는 방법


from collections import deque
import sys
filePath = "C:\\Users\khj77\\OneDrive\\바탕 화면\\Python\\python_Algo_practice\\Python-Algorithom\\1. 자료구조 활용(스택, 큐, 해쉬, 힙)\\input.txt"
sys.stdin = open(filePath, "rt")
n, m = map(int, input().split())
dqListTuple = [(idx, val) for idx, val in enumerate(list(map(int, input().split())))]
dq = deque(dqListTuple)

cnt = 0
while(dq):
	tmp = dq[0]
	maxTuple = max(dq, key=lambda x: x[1])
	if (tmp[1] == maxTuple[1]):
		cnt += 1
		if(dq[0][0] == m):
			dq.popleft()
			break
		else:
			dq.popleft()
	elif (tmp[1] != maxTuple[1]):
		dq.popleft()
		dq.append(tmp)
print(cnt)