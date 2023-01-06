import sys
filePath = "C:\\Users\khj77\\OneDrive\\바탕 화면\\Python\\python_Algo_practice\\Python-Algorithom\\1. 자료구조 활용(스택, 큐, 해쉬, 힙)\\input.txt"
sys.stdin = open(filePath, "rt")

num, k = map(int, input().split())
num = list(str(num))
stack = []
cnt = k

# solution
for x in num:
	while (stack and stack[-1] < x and cnt > 0): #stack이 비어있지 않고(==stack) and stack[-1] < x 이고 and cnt>0 인 경우에만 수행
		stack.pop()
		cnt -= 1
	stack.append(x)

'''
for i in range(len(num)):
	if (len(stack) == 0):
		stack.append(num[i])

	elif (cnt > 0):
		while (stack[-1] < num[i]):
			stack.pop()
			cnt -= 1
			if (len(stack) == 0 or cnt == 0):
				break
		stack.append(num[i])

	else:
		stack.append(num[i])
'''
if (cnt == 0):
	print("".join(stack))
else:
	print("".join(stack[:-cnt]))
