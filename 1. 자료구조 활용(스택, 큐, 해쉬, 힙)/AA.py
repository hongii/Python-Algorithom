import sys
# filePath = "C:\\Users\khj77\\OneDrive\\바탕 화면\\Python\\python_Algo_practice\\Python-Algorithom\\1. 자료구조 활용(스택, 큐, 해쉬, 힙)\\input.txt"
# sys.stdin = open(filePath, "rt")
inputList = list(input());

res = ""
stack = []
for x in inputList:
	if(x.isdecimal()):
		res += x
	else:
		if (x == "("):
			stack.append(x)
		elif (x == "*" or x == "/"):
			while (stack and (stack[-1] == "*" or stack[-1] == "/")):
				res += stack.pop()
			stack.append(x)
		elif(x == "+" or x == "-"):
			while (stack and stack[-1] != "("):
				res += stack.pop()
			stack.append(x)
		elif(x == ")"):
			while (stack[-1] != "("):
				res += stack.pop()
			stack.pop() # 여는 괄호("(") 제거
		
while(stack):
	res += stack.pop()

print(res)