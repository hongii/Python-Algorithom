from collections import deque
import sys
# filePath = "C:\\Users\khj77\\OneDrive\\바탕 화면\\Python\\python_Algo_practice\\Python-Algorithom\\1. 자료구조 활용(스택, 큐, 해쉬, 힙)\\input.txt"
# sys.stdin = open(filePath, "rt")
n, m = map(int, input().split())
dqListTuple = [(idx, val)
               for idx, val in enumerate(list(map(int, input().split())))]
dq = deque(dqListTuple)

cnt = 0
while (dq):
	tmp = dq[0]
	maxTuple = max(dq, key=lambda x: x[1])
	if (tmp[1] == maxTuple[1]):
		cnt += 1
		if (dq[0][0] == m):
			dq.popleft()
			break
		else:
			dq.popleft()
	elif (tmp[1] != maxTuple[1]):
		dq.popleft()
		dq.append(tmp)
print(cnt)
