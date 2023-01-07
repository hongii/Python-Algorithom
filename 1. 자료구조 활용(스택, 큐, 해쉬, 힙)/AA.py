import sys
# filePath = "C:\\Users\khj77\\OneDrive\\바탕 화면\\Python\\python_Algo_practice\\Python-Algorithom\\1. 자료구조 활용(스택, 큐, 해쉬, 힙)\\input.txt"
# sys.stdin = open(filePath, "rt")
inputList = list(input());

stack = []
for x in inputList:
	if(x.isdecimal()):
		stack.append(x)
	else:
		b = int(stack.pop())
		a = int(stack.pop())
		if(x == "+"):
			stack.append(a+b)
		elif(x == "-"):
			stack.append(a-b)
		elif (x == "*"):
			stack.append(a*b)
		elif(x == "/"):
			stack.append(a/b)

print(stack[0])