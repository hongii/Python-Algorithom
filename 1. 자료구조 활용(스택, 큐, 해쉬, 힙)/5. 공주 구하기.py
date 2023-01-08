### Queue 활용 ###
# <dequeue 라이브러리 사용> 
#    popleft  <--- ○○○○○○○○○○○○○○○○ --->  pop
# appendleft  ---> ○○○○○○○○○○○○○○○○ <--- append

# 다시 풀어볼 문제
from collections import deque
import sys
filePath = "C:\\Users\khj77\\OneDrive\\바탕 화면\\Python\\python_Algo_practice\\Python-Algorithom\\1. 자료구조 활용(스택, 큐, 해쉬, 힙)\\input.txt"
sys.stdin = open(filePath, "rt")
n, k = map(int, input().split())

cnt = k
dq = deque(list(range(1,n+1)))
while(len(dq) != 1):
	if(cnt > 0):
		x = dq.popleft()
		dq.append(x)
		cnt -= 1
	elif(cnt == 0):
		dq.pop()
		cnt = k 
print(dq[0])