import sys
filePath = "C:\\Users\khj77\\OneDrive\\바탕 화면\\Python\\python_Algo_practice\\Python-Algorithom\\2. 코드 구현력 기르기\\input.txt"
sys.stdin = open(filePath, "rt")

n = int(input())
solution = list(map(int, input().split()))
totalScore = 0
cnt = 0

for i in range(n):
	if (solution[i] == 0):
		cnt = 0
	else:
		cnt += 1
		totalScore += 1*cnt

print(totalScore)
