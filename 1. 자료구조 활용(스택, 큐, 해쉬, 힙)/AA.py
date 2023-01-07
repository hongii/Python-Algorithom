import sys
# filePath = "C:\\Users\khj77\\OneDrive\\바탕 화면\\Python\\python_Algo_practice\\Python-Algorithom\\1. 자료구조 활용(스택, 큐, 해쉬, 힙)\\input.txt"
# sys.stdin = open(filePath, "rt")
inputList = list(input())

stack = []
last = ""
totalCount = 0

for x in inputList:
	if (stack and x == ")"):
		if (last == "("):
			stack.pop()
			totalCount += len(stack)
		else:
			stack.pop()
			totalCount += 1
	else:
		stack.append(x)

	last = x

print(totalCount)
