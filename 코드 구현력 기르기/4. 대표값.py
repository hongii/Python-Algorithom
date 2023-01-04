import sys
filePath = "C:\\Users\khj77\\OneDrive\\바탕 화면\\Python\\python_Algo_practice\\Python-Algorithom\\코드 구현력 기르기\\input.txt"
sys.stdin = open(filePath,"rt");

n = int(input())
numList = list(map(int, input().split()))
avg = round(sum(numList) / n)
avg = int(avg+0.5) # 파이썬에서 round 함수는 round half even 방식을 채택하므로, 
									# round(66.5000) => 66이 된다.(짝수가 되려는 방향으로 올리거나 버림) 
									# 이를 방지하기 위해, 0.5를 더해서 정수부분을 1 증가시킨 후 int형으로 형변환 시키면 반올림하는 효과를 얻게된다. 

idx = 0
gap = abs(numList[0]-avg)
for i in range(1, n):
	if(abs(numList[i]-avg) < gap):
		idx = i 
		gap = abs(numList[i]-avg)
	elif(gap == abs(numList[i]-avg)):
		if(numList[i] > numList[idx]):
			idx = i

print(avg, idx+1)