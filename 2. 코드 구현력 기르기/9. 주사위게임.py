import sys
filePath = "C:\\Users\khj77\\OneDrive\\바탕 화면\\Python\\python_Algo_practice\\Python-Algorithom\\2. 코드 구현력 기르기\\input.txt"
sys.stdin = open(filePath, "rt")

n = int(input())
res = [0]*n

for i in range(n):
	numList = list(map(int, input().split()))

	if numList[0] == numList[1] and numList[0] == numList[2]:
		res[i] = 10000 + numList[0]*1000
	elif numList[0] == numList[1] or numList[0] == numList[2] or numList[1] == numList[2]:
		if numList[0] == numList[1] or numList[0] == numList[2]:
			res[i] = 1000 + numList[0]*100
		elif numList[1] == numList[2]:
			res[i] = 1000 + numList[1]*100
	else:
		res[i] = max(numList) * 100

print(max(res))
