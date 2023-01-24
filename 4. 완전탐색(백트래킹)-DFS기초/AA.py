n = int(input())
check = [0]*(n+1)

def dfs(x):
	if x > n:
		for i in range(1, n+1):
			if check[i] == 1:
				print(i, end=" ")
		print()
	else:
		check[x] = 1
		dfs(x+1)
		check[x] = 0
		dfs(x+1)


if __name__ == "__main__":
	dfs(1)


