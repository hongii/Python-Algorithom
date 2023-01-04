import sys
n, k = map(int, input().split())
numList = list(map(int, input().split()))

sum = set()
for i in range(n-2):
	for j in range(i+1, n-1):
		for m in  range(j+1, n):
			sum.add(numList[i]+numList[j]+numList[m])

sortedList = list(sum)
sortedList.sort(reverse=True)
print(sortedList[k-1])