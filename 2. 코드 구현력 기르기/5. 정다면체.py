import sys
# filePath = "C:\\Users\khj77\\OneDrive\\바탕 화면\\Python\\python_Algo_practice\\Python-Algorithom\\2. 코드 구현력 기르기\\input.txt"
# sys.stdin = open(filePath,"rt");

n, m = map(int, input().split())
sum = [[0]*(n+1) for _ in range(m+1)]
cnt = [0] * (n+m+1)

for i in range(1, m+1):
	for j in range(1, n+1):
		sum[i][j] = i+j
		cnt[i+j] += 1

maxNum = max(cnt)
for i in range(1, n+m+1):
	if(maxNum == cnt[i]):
		print(i,end=" ")