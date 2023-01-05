import sys
filePath = "C:\\Users\khj77\\OneDrive\\바탕 화면\\Python\\python_Algo_practice\\Python-Algorithom\\2. 코드 구현력 기르기\\input.txt"
sys.stdin = open(filePath,"rt");

count = 0
n, k = map(int, input().split())

for i in range(1,n+1):
	if(n % i == 0):
		count += 1
	if(count == k):
		print(i)
		break
else:
	print(-1)

