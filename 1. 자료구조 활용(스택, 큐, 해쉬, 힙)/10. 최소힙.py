import heapq as hq
import sys
filePath = "C:\\Users\khj77\\OneDrive\\바탕 화면\\Python\\python_Algo_practice\\Python-Algorithom\\1. 자료구조 활용(스택, 큐, 해쉬, 힙)\\input.txt"
sys.stdin = open(filePath, "rt")

heap = []
while True:
	num = int(input())
	if(num == -1):
		break
	if(num == 0):
		if(len(heap) == 0):
			print(-1)
		else:
			print(hq.heappop(heap)) # heap 리스트에서 root노드를 pop시키는 함수
	else:
		hq.heappush(heap, num) # heap 리스트에 num 값을 최소힙의 형태로 push 하는 함수

