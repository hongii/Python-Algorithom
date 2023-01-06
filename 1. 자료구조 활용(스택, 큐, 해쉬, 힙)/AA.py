import sys
# filePath = "C:\\Users\khj77\\OneDrive\\바탕 화면\\Python\\python_Algo_practice\\Python-Algorithom\\2. 코드 구현력 기르기\\input.txt"
# sys.stdin = open(filePath, "rt")

num, k = map(int, input().split())
num = list(str(num))
stack = []
cnt = k

for i in range(len(num)):
	if (len(stack) == 0):
		stack.append(num[i])

	elif(cnt > 0):
		while (stack[-1] < num[i]):
			stack.pop()
			cnt -= 1
			if (len(stack) == 0 or cnt == 0):
				break
		stack.append(num[i])
	
	else:
		stack.append(num[i])

if (cnt == 0):
	print("".join(stack))
else:
	print("".join(stack[:-cnt]))
