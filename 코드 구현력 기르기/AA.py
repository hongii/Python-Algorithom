import sys
# filePath = "C:\\Users\khj77\\OneDrive\\바탕 화면\\Python\\python_Algo_practice\\Python-Algorithom\\코드 구현력 기르기\\input.txt"
# sys.stdin = open(filePath,"rt");

n = int(input())
numList = list(map(int, input().split()))
avg = round(sum(numList) / n)

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