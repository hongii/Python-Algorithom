import sys
filePath = "C:\\Users\khj77\\OneDrive\\바탕 화면\\Python\\python_Algo_practice\\Python-Algorithom\\2. 코드 구현력 기르기\\input.txt"
sys.stdin = open(filePath,"rt");

n = int(input())
numList = map(str, input().split())

def isPrime(x):
	x = int(x)
	if (x == 1):
		return False
		
	for i in range(2, x):
		if(x % i == 0):
			return False
	else:
		return True

def reverse(x):
	reverseNumList = []
	for i in range(len(x), 0, -1):
		reverseNumList.append(x[i-1])
	return int(''.join(reverseNumList))


for x in numList:
	reverseNum = reverse(x)
	res = isPrime(reverseNum)
	if(res):
		print(reverseNum, end=" ")


